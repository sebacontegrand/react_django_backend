from rest_framework import serializers
from .models import Missions
from .models import Launches
class RtechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = ('id', 'title', 'description', 'image')
        read_only_fields = ('id',)
        
class LaunchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launches
        fields = ('id', 'name', 'rocket', 'youtube')
        read_only_fields = ('id',)