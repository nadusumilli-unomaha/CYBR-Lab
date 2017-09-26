from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views


#REST API routes
router = DefaultRouter(trailing_slash=False)

router.register(r'dogs', views.DogViewSet)
router.register(r'breeds', views.BreedViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]