from django.db import models


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(verbose_name='设备名', max_length=255)
    decription = models.TextField(default=None, verbose_name='设备使用')
    sum = models.IntegerField(verbose_name='设备总数')
    rest = models.IntegerField(verbose_name='设备剩余数')

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Reagent(models.Model):
    name = models.CharField(verbose_name='试剂名', max_length=255)
    decription = models.TextField(verbose_name='试剂使用说明', default=None)
    sum = models.IntegerField(verbose_name='试剂总数', default=0)
    rest = models.IntegerField(verbose_name='试剂剩余数', default=0)
    is_harm = models.BooleanField(default=True, choices=(('True', 'True'), ('False', 'False')))

    class Meta:
        verbose_name = '试剂信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(verbose_name='仪器名', max_length=255)
    decription = models.TextField(verbose_name='仪器使用', default=None)
    sum = models.IntegerField(verbose_name='仪器总数', default=0)
    rest = models.IntegerField(verbose_name='仪器剩余数', default=0)

    class Meta:
        verbose_name = '仪器信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
