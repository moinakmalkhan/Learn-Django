from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import RoomSerializer,CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class RoomView(generics.CreateAPIView,generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = "code"
    def get(self,request,format=None):
        code = request.GET.get(self.lookup_url_kwarg,None)
        if not code:
            return Response({"message":f"'{self.lookup_url_kwarg}' parameter is not found in url."},status=status.HTTP_400_BAD_REQUEST)
        room = Room.objects.filter(code=code)
        if len(room)>0:
            data = RoomSerializer(room[0]).data
            data['is_host'] = request.session.session_key == room[0].host
            return Response(data,status=status.HTTP_200_OK)
        return Response({"message":"Room not found."},status=status.HTTP_404_NOT_FOUND)

class JoinRoom(APIView):
    serializer_class = RoomSerializer
    def post(self,request,format=None):
        if not request.session.exists(request.session.session_key):
            request.session.create()
        code = request.data.get("code",None)
        if code:
            room = Room.objects.filter(code=code)
            if room.exists():
                request.session["room_code"] = code
                return Response({"message":"Room joined"},status=status.HTTP_200_OK)
            return Response({"message":"Room not found"},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"Room code is not given"},status=status.HTTP_400_BAD_REQUEST)

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self,request,format=None):
        if not request.session.exists(request.session.session_key):
            request.session.create()
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get("guest_can_pause")
            vote_to_skip = serializer.data.get("vote_to_skip")
            host = request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.vote_to_skip = vote_to_skip
                room.save(update_fields=["guest_can_pause","vote_to_skip"])
            else:
                room = Room(host=host,guest_can_pause=guest_can_pause,vote_to_skip=vote_to_skip)
                room.save()
            request.session["room_code"] = room.code
            return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInRoom(APIView):
    def get(self,request,format=None):
        if not request.session.exists(request.session.session_key):
            request.session.create()
        data={
            'code':request.session.get("room_code",None)
        }
        return JsonResponse(data,status=status.HTTP_200_OK)

class LeaveRoom(APIView):
    @csrf_exempt
    def get(self,request,format=None):
        if "room_code" in request.session:
            request.session.pop("room_code")
            host_id = request.session.session_key
            room = Room.objects.filter(host = host_id)
            if room.exists():
                room=room[0]
                room.delete()
        return Response({"message":"success"},status=status.HTTP_200_OK)