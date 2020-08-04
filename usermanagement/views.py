from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from usermanagement.models import HUser
from usermanagement.userhandler import UserHandler
class SignUp(View):
    def post(self, request):
        data = request.POST.dict()
        print(request.POST)


        #r = UserHandler()._validate(mobile=data["mobile"])
        r = HUser.objects.filter(mobile=data["mobile"])
        if r:
            messages.success(request, 'mobilenumber is already registered')
            return render(request, 'signup.html', {"massage": "already "})
        else:
            if data['password']== data['password2']:
                UserHandler().sign_up(mobile=data["mobile"], name=data["name"], password=data["password"], request=request)

                return redirect("/")
            else:
                messages.info(request,"passwords are not match")
                return render(request, 'signup.html')

    def get(self, request):
        return render(request, 'signup.html')


class LogIn(View):
    def post(self, request):
        data = request.POST.dict()
        print(request.POST)
        r=UserHandler().login(mobile=data["mobile"], password=data["password"], request=request)
        if r:
         return redirect("/chat/")
        else:

            messages.success(request,"Your mobile number or password is incorrect")
            return render(request, 'login.html')

    def get(self, request):
        return render(request, 'login.html')


class LogOut(View):
    def get(self, request):
        if not request.user.is_authenticated:
            redirect("/user/login")
        logout(request)
        return redirect('/')
