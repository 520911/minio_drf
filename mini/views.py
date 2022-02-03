from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from mini.serializers import FilesSerializer
from .models import FilesModel


class FilesViewSet(ModelViewSet):
    serializer_class = FilesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = FilesModel.objects.filter(user=self.request.user)
        return queryset
