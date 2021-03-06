# Generated by Django 3.0.3 on 2020-02-16 15:18

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Files",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "file",
                    models.FileField(help_text="uploaded zip file", upload_to="media/"),
                ),
                ("name", models.CharField(help_text="file name", max_length=255)),
                (
                    "uploaded_at",
                    models.DateTimeField(auto_now_add=True, help_text="time of upload"),
                ),
                (
                    "password",
                    models.CharField(
                        help_text="password required to allow user to download file",
                        max_length=15,
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="url that allows the user to download this file",
                        max_length=255,
                    ),
                ),
            ],
        ),
    ]
