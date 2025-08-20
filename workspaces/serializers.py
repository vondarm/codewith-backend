from .models import Workspace, User
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name']

class WorkspaceIdFilterSerializer(serializers.Serializer):
    workspace_id = serializers.IntegerField()
