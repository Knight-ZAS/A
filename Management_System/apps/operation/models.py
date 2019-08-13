from datetime import datetime

from django.db import models

from users.models import UserProfile
from items.models import Equipment, Reagent, Instrument
from lab.models import Laboratory
# Create your models here.


class LabReport(models.Model):
    title = models.CharField(verbose_name='标题', max_length=255)
    student = models.ForeignKey(UserProfile, verbose_name='学生', on_delete=models.CASCADE,
                                related_name='report_student_id')
    teacher = models.ForeignKey(UserProfile, verbose_name='教师', on_delete=models.CASCADE,
                                related_name='report_teacher_id')
    context = models.TextField(verbose_name='内容', default=None)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    score = models.IntegerField(verbose_name='分数', default=0)

    class Meta:
        verbose_name = '实验报告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Consume(models.Model):
    applicant = models.ForeignKey(UserProfile, verbose_name='申请人', on_delete=models.CASCADE, related_name='applicant_id')
    receiver = models.ForeignKey(UserProfile, verbose_name='接收人', on_delete=models.CASCADE, related_name='receiver_id')
    equipment = models.ForeignKey(Equipment, verbose_name='设备', on_delete=models.CASCADE)
    reagent = models.ForeignKey(Reagent, verbose_name='试剂', on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, verbose_name='仪器', on_delete=models.CASCADE)
    equip_num = models.IntegerField(verbose_name='设备损坏数量', default=0)
    reagent_num = models.IntegerField(verbose_name='试剂消耗数量', default=0)
    instrument_num = models.IntegerField(verbose_name='仪器损坏数量', default=0)
    addition = models.TextField(verbose_name='备注', null=True, blank=True)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    is_approve = models.BooleanField(default=True, choices=(('True', 'True'), ('False', 'False')))

    class Meta:
        verbose_name = '耗材报告'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.applicant


class Course(models.Model):
    student = models.ForeignKey(UserProfile, verbose_name='学生', on_delete=models.CASCADE,
                                related_name='course_student_id')
    teacher = models.ForeignKey(UserProfile, verbose_name='教师', on_delete=models.CASCADE,
                                related_name='course_teacher_id')
    experimenter = models.ForeignKey(UserProfile, verbose_name='实验员', null=True, blank=True, on_delete=models.CASCADE,
                                     related_name='experimenter_id')
    lab_manager = models.ForeignKey(UserProfile, verbose_name='大型设备实验员', null=True, blank=True,
                                    on_delete=models.CASCADE, related_name='manager_id')
    name = models.CharField(verbose_name='名称', max_length=255)
    credits = models.FloatField(verbose_name='学分', max_length=5)
    laboratory = models.ForeignKey(Laboratory, verbose_name='实验室', on_delete=models.CASCADE)
    day = models.CharField(verbose_name='日', max_length=9, default='Monday', choices=(
        ('Monday', '周一'),
        ('Tuesday', '周二'),
        ('Wednesday', '周三'),
        ('Thursday', '周四'),
        ('Friday', '周五'),
        ('Saturday', '周六'),
        ('Sunday', '周日'),
    ))
    section = models.CharField(verbose_name='节次', max_length=5, default='one', choices=(
        ('one', '第一节'),
        ('two', '第二节'),
        ('three', '第三节'),
        ('four', '第四节'),
        ('five', '第五节'),
        ('six', '第六节'),
        ('seven', '第七节'),
        ('eight', '第八节'),
        ('nine', '第九节'),
        ('ten', '第十节'),
    ))

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class UserSchedule(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='年份')
    term = models.CharField(verbose_name='季度', max_length=5)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class LabSchedule(models.Model):
    user = models.ForeignKey(Laboratory, verbose_name='实验室', on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name='年份')
    term = models.CharField(verbose_name='季度', max_length=5)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '实验室课表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = '板块'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=255, unique=True)
    category = models.ForeignKey(Category, verbose_name='板块', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='图片', max_length=255, null=True, blank=True, upload_to='image/%Y',
                              default='image/2019/image.png')
    content = models.TextField(verbose_name='内容', default=None)
    author = models.OneToOneField(UserProfile, verbose_name="作者", on_delete=models.CASCADE)
    publish_date = models.DateTimeField(verbose_name="发布日期", auto_now=True)
    hidden = models.BooleanField(default=False, verbose_name="是否隐藏")
    priority = models.IntegerField(default=1000, verbose_name="优先级")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "<%s,author:%s>" % (self.title, self.author)


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, verbose_name='评论者', on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024, default=None)
    date = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', related_name='p_comment', blank=True, null=True,
                                       on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "<user:%s>" % self.user


class ThumbUp(models.Model):
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='点赞者')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '点赞信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.article
