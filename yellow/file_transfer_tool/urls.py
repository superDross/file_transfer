from django.urls import path, re_path

from . import views

app_name = "file_transfer_tool"

urlpatterns = [
    path("upload/", views.Upload.as_view(), name="upload"),
    re_path(r"^download/(?P<id>(.*))/", views.Download.as_view(), name="download"),
]
