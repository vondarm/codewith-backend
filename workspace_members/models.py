from django.db import models
from workspaces.models import Workspace
from users.models import User

class WorkspaceMember(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Владелец'),
        ('editor', 'Редактор'),
        ('viewer', 'Пользователь'),
    ]

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('workspace', 'user')
