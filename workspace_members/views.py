from rest_framework import viewsets, permissions, serializers
from rest_framework.views import APIView
from workspaces.serializers import WorkspaceIdFilterSerializer
from .models import WorkspaceMember
from .serializers import WorkspaceMemberSerializer


class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        serializer = WorkspaceIdFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        workspace_id = serializer.validated_data['workspace_id']
        return WorkspaceMember.objects.filter(workspace_id=workspace_id)

    permission_classes = [permissions.AllowAny]
    serializer_class = WorkspaceMemberSerializer
