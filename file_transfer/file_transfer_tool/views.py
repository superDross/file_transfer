# from django.views.generic.edit import FormView
# from file_transfer_tool.forms import UploadFileForm


# class Upload(FormView):
#     template_name = "file_transfer_tool/upload.html"
#     form_class = UploadFileForm
#     success_url = "/upload/"

from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import DownloadForm, UploadFileForm
from .models import Files

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=True)
            download_url = f"{request.get_host()}/download/{file.id}/"
            return render(
                request=request,
                template_name="file_transfer_tool/successful_upload.html",
                context={'file': file, 'download_url': download_url}
            )
    else:
        form = UploadFileForm()
    return render(
        request=request,
        template_name="file_transfer_tool/upload.html",
        context={"form": form},
    )


def download_page(request, obj_id):
    if request.method == "POST":
        form = DownloadForm(request.POST)
        if form.is_valid():
            given_password = form["password"].value()
            file = Files.objects.get(id=obj_id)
            if file.password != given_password:
                return render(
                    request=request,
                    template_name="file_transfer_tool/invalid_password.html",
                    context={"form": form},
                )
            filename = file.file.name.split("/")[-1]
            response = HttpResponse(file.file, content_type="text/plain")
            response["Content-Disposition"] = f"attachment; filename={filename}"
            return response
    else:
        if not file_exists(obj_id):
            return render(
                request=request,
                template_name="file_transfer_tool/does_not_exist.html",
                context={"object_identity": obj_id},
            )
        form = DownloadForm()
    return render(request, "file_transfer_tool/download_password.html", {"form": form})


def file_exists(obj_id):
    try:
        Files.objects.get(id=obj_id)
        return True
    except (Files.DoesNotExist, ValidationError):
        return False
