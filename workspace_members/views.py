from rest_framework import viewsets, permissions, serializers
from rest_framework.views import APIView, Response, status
from workspaces.serializers import WorkspaceIdFilterSerializer
from .models import WorkspaceMember
from .serializers import WorkspaceMemberSerializer, WorkspaceMemberCreateSerializer


class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        serializer = WorkspaceIdFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        workspace_id = serializer.validated_data['workspace_id']
        return WorkspaceMember.objects.filter(workspace_id=workspace_id)

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkspaceMemberCreateSerializer
        return WorkspaceMemberSerializer

    def destroy(self, request, pk):
        instance = WorkspaceMember.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #TODO
    permission_classes = [permissions.IsAuthenticated]
