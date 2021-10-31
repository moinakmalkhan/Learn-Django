from django.shortcuts import HttpResponse
# def my_middleware(get_response):
#     # Here we write the code that we want to execute when server start runing. this code will run only one time when server start running
#     print("Server is started - from my_middleware")
#     def viewfunctions(request):
#         # here we write code that we wanna execute before view function execution
#         print("Before view function execution ")
#         response = get_response(request)
#         # here we write code that we wanna execute after view function execution
#         print("After view function execution ")
#         return response
#     return viewfunctions



# class MyMiddleWare1:
#     """ Class based middleware """
#     def __init__(self, get_response):
#         """this function will run only one time when server start"""
#         self.get_response = get_response
#         print("Middleware1 Initialization")
#     def __call__(self, request):
#         """ This part of code will run before execution of view function """
#         print("Hello From middleware1 before exection of view funtion")
#         response = self.get_response(request)
#         # """ we can send directly response to user without execute any other middle ware """
#         # response = HttpResponse("Response from middleware1")
#         """ This part of code will run After execution of view function """
#         print("Hello From middleware1 After exection of view funtion")
#         return response




# class MyMiddleWare2:
#     """ Class based middleware """
#     def __init__(self, get_response):
#         """this function will run only one time when server start"""
#         self.get_response = get_response
#         print("Middleware2 Initialization")
#     def __call__(self, request):
#         """ This part of code will run before execution of view function """
#         print("Hello From middleware2 before exection of view funtion")
#         # response = self.get_response(request)
#         """ we can send directly response to user without execute any other middle ware """
#         response = HttpResponse("Response from middleware2")

#         """ This part of code will run After execution of view function """
#         print("Hello From middleware2 After exection of view funtion")
#         return response



# class MyMiddleWare3:
#     """ Class based middleware """
#     def __init__(self, get_response):
#         """this function will run only one time when server start"""
#         self.get_response = get_response
#         print("Middleware3 Initialization")
#     def __call__(self, request):
#         """ This part of code will run before execution of view function """
#         print("Hello From middleware3 before exection of view funtion")
#         response = self.get_response(request)
#         """ This part of code will run After execution of view function """
#         print("Hello From middleware3 After exection of view funtion")
#         return response





class MyMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    def process_exception(self, request, exception):
        msg = exception
        class_name = exception.__class__.__name__
        print("class name : ",class_name)
        print("msg : ",msg)
        return HttpResponse(msg)
        
