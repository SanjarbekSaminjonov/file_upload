from rest_framework.viewsets import ModelViewSet
from .models import File
from .serializers import FileSerializer

# Create your views here.


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
