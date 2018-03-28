from django.contrib import admin
from favurls.models import UrlClassify, UrlManager


class UrlClassifyAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'creator')
    search_fields = ('type_name', )


class UrlManagerAdmin(admin.ModelAdmin):
    list_display = ('url_name', 'url_link', 'classify', 'creator', 'create_time')
    search_fields = ('url_name', 'classify')
    list_filter = ('classify', 'creator')


admin.site.register(UrlClassify, UrlClassifyAdmin)
admin.site.register(UrlManager, UrlManagerAdmin)

admin.site.site_header = '速易捷后台管理'
admin.site.site_title = '速易捷'
