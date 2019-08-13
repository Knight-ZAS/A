# _*_ encoding:utf-8 _*_
from functools import wraps
from django.shortcuts import render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.backends import  ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from users.models import UserProfile
from users.forms import LoginForm

class LoginView(View):
    def get(self,request):
        return render(request, "login.html")
    def post(self,request):
        # login_form = LoginForm(request.POST)
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request,user)
            if user.identity == 'student':
                return render(request,"student.html")
            elif user.identity == 'teacher':
                return render(request,"teacher.html")
            elif user.identity == 'experimenter':
                return render(request,"experimenter.html")
            elif user.identity == 'lab_manager':
                return render(request,"lab_manager.html")
            elif user.identity == 'administrator':
                return render(request,"administrator.html")
            elif user.identity == 'leader':
                return render(request,"leader.html")
            else :
                return render(request, "login.html", {"msg": "用户名或密码错误"})

        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
