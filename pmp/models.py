from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class PMPDescription(models.Model):
    long_EN = models.CharField(max_length=50, null=False, unique=True, blank=False, verbose_name='英文全称')
    long_CN = models.CharField(max_length=50, null=False, blank=False, verbose_name='中文全称')
    short = models.CharField(max_length=10, default='-', null=False, blank=False, verbose_name='英文缩写')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='术语解释')
    version = models.CharField(max_length=15, default='第六版', null=True, blank=True, verbose_name='PMBOK版本')

    class Meta:
        verbose_name = 'PMP术语'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.long_EN


class AboutMe(models.Model):
    photo = models.ImageField(upload_to='photo', verbose_name='头像')
    peer = models.CharField(max_length=100, verbose_name='职业')
    email = models.EmailField(verbose_name='电子邮箱')
    summary = RichTextField(max_length=2000, verbose_name='简介')
    createdate = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    lastupdate = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.peer


class Declare(models.Model):
    content = RichTextField(max_length=2000, verbose_name='申明内容')
    createdate = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    lastupdate = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    wechar = models.ImageField(upload_to='wechar', null=True, blank=True, verbose_name='微信收款码')
    zifubao = models.ImageField(upload_to='zhifubao', null=True, blank=True, verbose_name='支付宝收款码')

    class Meta:
        verbose_name = '申明'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
