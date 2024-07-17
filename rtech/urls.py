from rest_framework import routers
from .api import MissionsViewSet
from .api import LaunchesViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('api/missions', MissionsViewSet,'missions')
router.register('api/launches', LaunchesViewSet,'launches')
urlpatterns = router.urls




