from wechart.models import WXDevInfo
from django.contrib import admin


class WXDevInfoAdmin(admin.ModelAdmin):
    list_display = ('AppId', 'AppSecret')


admin.site.register(WXDevInfo, WXDevInfoAdmin)