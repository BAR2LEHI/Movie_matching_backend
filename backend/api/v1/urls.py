from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from .views import MovieViewSet, GenreViewSet, UserViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('movies', MovieViewSet, basename='movies')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router_v1.urls))
]




