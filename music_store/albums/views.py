from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from .serializers import *

# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('name')
    serializer_class = AlbumSerializer
    permission_classes = []

class AlbumGenreViewSet(viewsets.ModelViewSet):
    queryset = AlbumGenre.objects.all()
    serializer_class = AlbumGenreSerializer
    permission_classes = []

class AlbumSongsViewSet(viewsets.ModelViewSet):
    queryset = AlbumSongs.objects.all()
    serializer_class = AlbumSongsSerializer
    permission_classes = []
