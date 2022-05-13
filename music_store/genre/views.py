from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from .serializers import *

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = []