from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from mini.serializers import FilesSerializer
from .models import FilesModel


class FilesViewSet(ModelViewSet):
    serializer_class = FilesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = FilesModel.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = ''
        for item in serializer.data:
            data += item['file_path'].split('/')[-1] + ', '
        return JsonResponse({'file_list': data.strip(', ')})


class DownloadFile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if {'name'}.issubset(request.data):
            user = self.request.user
            return JsonResponse(
                {'Download link': settings.MINIO_STORAGE_MEDIA_URL + f'/{user.id}/{request.data["name"]}'})
        else:
            return JsonResponse({'Need all fields': 'id, name'})
