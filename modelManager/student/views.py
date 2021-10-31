from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    # stu=Student.students.all()
    stu=Student.students.get_roll_range(101,103)
    context={"students":stu}
    return render(request,"student/index.html",context)