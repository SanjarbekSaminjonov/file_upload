from django.contrib import admin
from .models import File

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'file_size', 'id',)
    list_filter = ('file_type',)


admin.site.register(File, FileAdmin)
