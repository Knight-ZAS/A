"""Management_System URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Management_System.settings")# project_name 项目名称
django.setup()
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from apps.items.views import getform
from django.views.generic import TemplateView
import xadmin
from django.urls import path, include
from users.views import LoginView
from users.views import login
from django.views.generic.base import View

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name="login.html"),name="login"),
    path('login/', LoginView.as_view(), name="login"),
]