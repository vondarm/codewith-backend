from django.db import models
from workspaces.models import Workspace
from users.models import User
from rooms.models import Room

class RoomMember(models.Model):
    display_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
