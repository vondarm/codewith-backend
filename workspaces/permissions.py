from rest_framework import permissions
from .models import Workspace
from workspace_members.models import WorkspaceMember

class WorkspacePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            member = WorkspaceMember.objects.get(workspace=obj, user=request.user)
            return member.role == 'owner'
        except WorkspaceMember.DoesNotExist:
            return False
