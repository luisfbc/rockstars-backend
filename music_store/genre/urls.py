from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'',views.GenreViewSet)

urlpatterns = [
	#path('thing', views.ThingView.as_view()),
	path('', include(router.urls)),
]