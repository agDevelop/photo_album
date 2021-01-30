from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.http import JsonResponse
from album.models import Album, Size, Binding, Template
from .serializer import AlbumSerializer, SizeSerializer, BindingSerializer, TemplateSerializer



class AlbumViewset(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        album = Album.objects.all()
        return album


class SizeViewset(viewsets.ModelViewSet):
    serializer_class = SizeSerializer

    def get_queryset(self):
        size = Size.objects.all()
        return size

class BindingViewset(viewsets.ModelViewSet):
    serializer_class = BindingSerializer

    def get_queryset(self):
        binding = Binding.objects.all()
        return binding


class TemplateViewset(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer

    def get_queryset(self):
        template = Template.objects.all()
        return template

