from django.db import models
from django.contrib.auth.models import User


class UrlClassify(models.Model):
    """ URL分类 """
    type_code = models.CharField(max_length=20, primary_key=True, verbose_name='url分类编码')
    type_name = models.CharField(max_length=40, unique=True, verbose_name='url分类名称')
    creator = models.ForeignKey(User, verbose_name='创建人')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = 'URL分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class UrlManager(models.Model):
    """ URL管理 """
    url_name = models.CharField(max_length=100, unique=True, verbose_name='URL名称')
    url_link = models.URLField(max_length=200, unique=True, verbose_name='URL地址')
    classify = models.ForeignKey(UrlClassify, verbose_name='分类')
    note = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')
    creator = models.ForeignKey(User, verbose_name='创建者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = 'URL管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url_name


