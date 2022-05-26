from rest_framework.viewsets import ModelViewSet
from .models import File
from .serializers import FileSerializer

# Create your views here.


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return File.objects.filter(author=self.request.user)
        return File.objects.none()
