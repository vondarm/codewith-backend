from rest_framework import viewsets, permissions
from .models import Workspace
from workspace_members.models import WorkspaceMember
from .serializers import WorkspaceSerializer
from .permissions import HasWorkspacePermissions


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        workspace = serializer.save()
        WorkspaceMember.objects.create(
            workspace=workspace,
            user=self.request.user,
            role='owner'
        )
