from .models import RoomMember
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMember
        fields = ['id', 'display_name', 'user']

    def create(self, validated_data):
        request = self.context['request']
        if request.user.is_authenticated:
            validated_data['user'] = request.user
            validated_data['display_name'] = None
        return super().create(validated_data)
