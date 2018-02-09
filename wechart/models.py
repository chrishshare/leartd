from django.db import models


class WXDevInfo(models.Model):
    AppId = models.CharField(max_length=20, verbose_name='开发者ID(AppID)')
    AppSecret = models.CharField(max_length=50, verbose_name='开发者密码(AppSecret)')
    accesstoken = models.CharField(max_length=256, verbose_name='ACCESSTOKEN')

    class Meta:
        verbose_name = '微信公众号基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.AppId
