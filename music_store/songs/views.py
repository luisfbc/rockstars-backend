from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from .serializers import *

# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer
    permission_classes = []

class SongsGenreViewSet(viewsets.ModelViewSet):
    queryset = SongsGenre.objects.all()
    serializer_class = SongsGenreSerializer
    permission_classes = []

