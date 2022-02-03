from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return '/'.join([str(instance.user.id), filename])


class FilesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_file')
    file_path = models.FileField(upload_to=user_directory_path, max_length=255, null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User file'
        verbose_name_plural = 'User files'

    def __str__(self):
        return f'{self.user.id}'
