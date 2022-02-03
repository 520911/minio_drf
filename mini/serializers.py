from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import FilesModel


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class FilesSerializer(ModelSerializer):

    class Meta:
        model = FilesModel
        fields = ('file_path',)
