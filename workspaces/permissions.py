from rest_framework import permissions
from .models import Workspace

class HasWorkspacePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # if view.action == 'create':
        #     return request.user and request.user.is_authenticated
        return True
    #
    # def has_object_permission(self, request, view, obj):
    #     return True
    #     if request.method in permissions.SAFE_METHODS:
    #         return request.user and request.user.is_authenticated
    #
    #     try:
    #         member = WorkspaceMember.objects.get(workspace=obj, user=request.user)
    #         return member.role == 'owner'
    #     except WorkspaceMember.DoesNotExist:
    #         return False



class HasWorkspaceMembersPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        workspace_id = view.kwargs.get('workspace_pk')
        if not request.user.is_authenticated:
            return False

        try:
            member = WorkspaceMember.objects.get(
                workspace_id=workspace_id,
                user=request.user
            )
            return member.role == 'owner'
        except WorkspaceMember.DoesNotExist:
            return False