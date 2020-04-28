from rest_framework import routers
from .views import UserViewSet, EntryViewSet,SyainViewSet,Syain2ViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'syains', SyainViewSet)
router.register(r'syain2s', Syain2ViewSet)
