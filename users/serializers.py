from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'display_name', 'id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AnonimousRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name', 'id']

    def create(self, validated_data):
        return User.objects.create_anonymous(**validated_data)
