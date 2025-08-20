from rest_framework import viewsets, permissions
from .models import Room
from .serializers import RoomSerializer
from workspaces.serializers import WorkspaceIdFilterSerializer


class RoomViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        serializer = WorkspaceIdFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        workspace_id = serializer.validated_data['workspace_id']
        return Room.objects.filter(workspace_id=workspace_id)

    permission_classes = [permissions.AllowAny]
    serializer_class = RoomSerializer
