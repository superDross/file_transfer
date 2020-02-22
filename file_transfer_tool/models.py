import uuid

from django.contrib.auth.models import User
from django.db import models


class Files(models.Model):
    """
    File that a user uploads
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="media/", help_text="uploaded zip file")
    name = models.CharField(max_length=255, help_text="file name")
    uploaded_at = models.DateTimeField(auto_now_add=True, help_text="time of upload")
    password = models.CharField(
        max_length=255, help_text="password required to allow user to download file"
    )

    def __str__(self) -> str:
        return self.name
