from django.contrib import admin
from pmp.models import PMPDescription


class PMPDescriptionAdmin(admin.ModelAdmin):
    list_display = ('long_EN', 'short', 'long_CN', 'version')


admin.site.register(PMPDescription, PMPDescriptionAdmin)


