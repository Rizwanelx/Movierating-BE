from django.conf.urls import url, include
from rest_framework import routers
from MovieRaterApi.api import views
from MovieRaterApi.api.views import CustomObtainAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'ratings', views.RatingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]