from rest_framework import viewsets
from .models import RoomMember
from .serializers import RoomMemberSerializer
from rooms.serializers import RoomIdFilterSerializer

class RoomMemberViewSet(viewsets.ModelViewSet):
    serializer_class = RoomMemberSerializer

    def get_queryset(self):
        serializer = RoomIdFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        room_id = serializer.validated_data['room_id']
        return RoomMember.objects.filter(room_id=room_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
