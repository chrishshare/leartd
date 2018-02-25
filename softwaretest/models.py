from django.db import models

# Create your models here.


class SoftwareTest(models.Model):
    long_EN = models.CharField(max_length=50, null=False, blank=False, verbose_name='英文全称')
    short = models.CharField(max_length=10, default='-', null=True, blank=True, verbose_name='英文缩写')
    long_CN = models.CharField(max_length=50, null=False, blank=False, verbose_name='中文全称')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='术语解释')
    keyword = models.CharField(max_length=15, null=True, blank=True, verbose_name='关键词')

    class Meta:
        verbose_name = 'ISTQB(软件测试)术语表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.long_EN