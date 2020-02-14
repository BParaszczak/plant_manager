from django.urls import include, path
from rest_framework import routers
from . import views

# def router robi za nas widoki generowane przez nasz viewset; tworzy do nich ścieżki
router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('rooms', views.RoomViewSet)
router.register('plants', views.PlantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
