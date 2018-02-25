from django.contrib import admin
from softwaretest.models import SoftwareTest


class SoftwareTestAdmin(admin.ModelAdmin):
    list_display = ('long_EN', 'short', 'long_CN', 'keyword')


admin.site.register(SoftwareTest, SoftwareTestAdmin)

