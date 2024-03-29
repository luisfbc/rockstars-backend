from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="MusicStore API",
      default_version='v1.2.0',
      description="Music Store API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@musicstore.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('music_store.users.urls')),
    path('songs/', include('music_store.songs.urls')),
    path('albums/', include('music_store.albums.urls')),
    path('genres/', include('music_store.genre.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




