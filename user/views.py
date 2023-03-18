from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('TaskList')
        else:
            return render(request, 'login.html', {})

    def post(self, request):
        context = {}
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(raw_password, user.password):
                login(request, user)
                return redirect('TaskList')
            else:
                context["msg"] = "Invalid Password!"
        except:
            context['msg'] = "Invalid Username!"
        return render(request, 'login.html', context)


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('Login')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html', {})

    def post(self, request):
        firstname = request.POST.get('firstname', "")
        lastname = request.POST.get('lastname', "")
        email = request.POST.get('email', "")
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        user = User(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
        user.save()
        login(request, user)
        return redirect('TaskList')
