from django.conf.urls import url, include
from rest_framework import routers
from drf_demo.views import UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
	url(r'/', include(router.urls)),
]