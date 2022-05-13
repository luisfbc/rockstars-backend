from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'songs',views.AlbumSongsViewSet)
router.register(r'genre',views.AlbumGenreViewSet)
router.register(r'',views.AlbumViewSet)

urlpatterns = [
	#path('thing', views.ThingView.as_view()),
	path('', include(router.urls)),
]