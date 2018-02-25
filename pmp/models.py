from django.db import models

# Create your models here.


class PMPDescription(models.Model):
    long_EN = models.CharField(max_length=50, null=False, blank=False, verbose_name='英文全称')
    long_CN = models.CharField(max_length=50, null=False, blank=False, verbose_name='中文全称')
    short = models.CharField(max_length=10, default='-', null=False, blank=False, verbose_name='英文缩写')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='术语解释')
    version = models.CharField(max_length=15, default='第五版', null=True, blank=True, verbose_name='PMBOK版本')

    class Meta:
        verbose_name = 'PMP术语'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.long_EN
