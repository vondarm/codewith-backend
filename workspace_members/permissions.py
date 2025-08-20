from rest_framework import permissions
from .models import Workspace

class WorkspaceMembersPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        workspace_id = view.kwargs.get('workspace_pk')

        try:
            member = WorkspaceMember.objects.get(
                workspace_id=workspace_id,
                user=request.user
            )
            return member.role == 'owner'
        except WorkspaceMember.DoesNotExist:
            return False