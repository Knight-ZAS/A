# _*_ encoding:utf-8 _*_
# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    name = models.CharField(verbose_name='姓名', max_length=255)
    gender = models.CharField(verbose_name='性别', choices=(
        ('male', '男'),
        ('female', '女')
    ),
                              max_length=6, default='male')
    identity = models.CharField(verbose_name='身份', choices=(
        ('student', '学生'),
        ('teacher', '授课教师'),
        ('experimenter', '实验员'),
        ('lab_manager', '实验管理员'),
        ('administrator', '管理员'),
        ('leader', '分管领导')
    ),
                                max_length=13, default='student')
    major = models.CharField(verbose_name='专业', max_length=255, null=True, default='')
    Class = models.IntegerField(verbose_name='班级', default=0)
    head_image = models.ImageField(verbose_name='头像', max_length=255, upload_to='head_image/%Y',
                                   default='head_image/2019/head.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.num
