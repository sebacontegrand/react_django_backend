from rest_framework import viewsets,permissions
from .models import Missions
from .models import Launches
from .serializers import RtechSerializer
from .serializers import LaunchesSerializer

class MissionsViewSet(viewsets.ModelViewSet):
    queryset = Missions.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RtechSerializer

class LaunchesViewSet(viewsets.ModelViewSet):
    queryset = Launches.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = LaunchesSerializer