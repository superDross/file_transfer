from django.contrib.auth.models import User
from django.db import models


class Files(models.Model):
    """
    File that a user uploads
    """

    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="media/", help_text="uploaded zip file")
    name = models.CharField(max_length=255, help_text="file name")
    uploaded_at = models.DateTimeField(auto_now_add=True, help_text="time of upload")
    password = models.CharField(
        max_length=15, help_text="password required to allow user to download file"
    )
    url = models.CharField(
        max_length=255, help_text="url that allows the user to download this file"
    )
    # change auto now add
    valid_until = models.DateTimeField(
        auto_now_add=True, help_text="download expiration date"
    )

    def __str__(self):
        return self.name