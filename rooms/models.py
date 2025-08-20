from django.db import models
from workspaces.models import Workspace
import uuid

class Room(models.Model):
    room_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    name = models.CharField(max_length=100, blank=True)
    environment_id = models.CharField(max_length=100, blank=True)
    code = models.TextField(blank=True)
    description = models.TextField(blank=True)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
