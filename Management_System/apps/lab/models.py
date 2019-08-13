from django.db import models


# Create your models here.
class Laboratory(models.Model):
    address = models.CharField(verbose_name='地点', max_length=255)
    administrator = models.CharField(verbose_name='实验员', null=True, blank=True, max_length=255)
    name = models.CharField(null=True, verbose_name='实验室名称', max_length=255)

    class Meta:
        verbose_name = '实验室信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.address
