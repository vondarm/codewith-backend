from rest_framework import viewsets, permissions
from rest_framework.views import Response, status
from room_member.models import RoomMember
from .models import Room
from .serializers import RoomSerializer, RoomCreateSerializer
from workspaces.serializers import WorkspaceIdFilterSerializer


class RoomViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        serializer = WorkspaceIdFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        workspace_id = serializer.validated_data['workspace_id']
        return Room.objects.filter(workspace_id=workspace_id)

    def get_serializer_class(self):
        if self.action == 'create':
            return RoomCreateSerializer
        return RoomSerializer

    def destroy(self, request, pk):
        instance = Room.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [permissions.AllowAny]
    serializer_class = RoomSerializer
