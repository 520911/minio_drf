from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import FilesModel


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class FilesSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = FilesModel
        fields = ('user', 'file_path', 'create_dt')

