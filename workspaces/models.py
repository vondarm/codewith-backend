from django.db import models
from users.models import User

class Workspace(models.Model):
    name = models.CharField(max_length=100)
    # МБ это поле не нужно
    members = models.ManyToManyField(
        User,
        through='workspace_members.WorkspaceMember',
        related_name='workspaces'
    )

    def __str__(self):
        return self.name
