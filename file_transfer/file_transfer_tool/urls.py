from django.urls import path, re_path

from . import views

app_name = "file_transfer_tool"

urlpatterns = [
    path("upload/", views.upload_file, name="upload"),
    re_path(r"^download/(.*)/", views.download_page, name="download"),
]
