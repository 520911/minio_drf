from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mini.views import FilesViewSet, DownloadFile

router = DefaultRouter()
router.register('files', FilesViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
    path('download/', DownloadFile.as_view()),
]
