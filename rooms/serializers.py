from workspaces.models import Workspace
from .models import Room
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    workspace = serializers.PrimaryKeyRelatedField(queryset=Workspace.objects.all())
    class Meta:
        model = Room
        fields = ['id', 'room_id', 'environment_id', 'workspace', 'code']
