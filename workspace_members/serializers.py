from .models import WorkspaceMember, User, Workspace
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class WorkspaceMemberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    role = serializers.ChoiceField(choices=WorkspaceMember.ROLE_CHOICES)
    display_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = WorkspaceMember
        fields = ['id', 'user', 'role', 'workspace', 'display_name', 'email']

    def get_display_name(self, member):
        return str(member.user) if member.user else None

    def get_email(self, member):
        return member.user.email

class WorkspaceMemberCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    workspace_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WorkspaceMember
        fields = ['email', 'workspace_id', 'role']

    def validate(self, attrs):
        email = attrs.get('email')
        workspace_id = attrs.get('workspace_id')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'Пользователь с таким email не найден'})

        try:
            workspace = Workspace.objects.get(id=workspace_id)
        except Workspace.DoesNotExist:
            raise serializers.ValidationError({'workspace_id': 'Рабочее пространство не найдено'})

        if WorkspaceMember.objects.filter(workspace=workspace, user=user).exists():
            raise serializers.ValidationError('Пользователь уже является участником пространства')

        attrs['user'] = user
        attrs['workspace'] = workspace
        return attrs

    def create(self, validated_data):
        return WorkspaceMember.objects.create(
            user=validated_data['user'],
            workspace=validated_data['workspace'],
            role=validated_data['role']
        )
