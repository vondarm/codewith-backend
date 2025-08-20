from .models import WorkspaceMember, User
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class WorkspaceMemberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    role = serializers.ChoiceField(choices=WorkspaceMember.ROLE_CHOICES)
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = WorkspaceMember
        fields = ['id', 'user', 'role', 'workspace', 'display_name']

        validators = [
            UniqueTogetherValidator(
                queryset=WorkspaceMember.objects.all(),
                fields=['workspace', 'user'],
                message="Этот пользователь уже добавлен в рабочее пространство."
            )
        ]

    def get_display_name(self, member):
        return str(member.user) if member.user else None
