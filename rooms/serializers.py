from workspaces.models import Workspace
from .models import Room
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'public_id', 'environment_id', 'code']

class RoomCreateSerializer(serializers.ModelSerializer):
    workspace_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Room
        fields = ['environment_id', 'name', 'workspace_id']

    def validate(self, attrs):
        workspace_id = attrs.get('workspace_id')
        print(workspace_id, attrs)
        try:
            workspace = Workspace.objects.get(id=workspace_id)
        except Workspace.DoesNotExist:
            raise serializers.ValidationError({'workspace_id': 'Рабочее пространство не найдено'})

        attrs['workspace'] = workspace
        return attrs

    def create(self, validated_data):
        return Room.objects.create(
            workspace=validated_data['workspace'],
            environment_id=validated_data['environment_id'],
            name=validated_data['name']
        )

class RoomIdFilterSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
