from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet


router = DefaultRouter()
router.register('', FileViewSet, basename='file')


urlpatterns = [
    path('', include(router.urls)),
]
