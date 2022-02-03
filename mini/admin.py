from django.contrib import admin
from .models import FilesModel


@admin.register(FilesModel)
class FilesAdmin(admin.ModelAdmin):
    pass

