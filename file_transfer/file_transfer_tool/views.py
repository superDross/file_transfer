# from django.views.generic.edit import FormView
# from file_transfer_tool.forms import UploadFileForm


# class Upload(FormView):
#     template_name = "file_transfer_tool/upload.html"
#     form_class = UploadFileForm
#     success_url = "/upload/"

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from .models import Files

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        # something would need to validate file type
        if form.is_valid():
            form.save(commit=True)
            # go to page showing an upload link
            return HttpResponseRedirect("/upload/")
    else:
        form = UploadFileForm()
    return render(request, "file_transfer_tool/upload.html", {"form": form})


def download_file(request, obj_id):
    if request.method == "GET":
        try:
            file = Files.objects.get(id=obj_id)
            filename = file.file.name.split("/")[-1]
            response = HttpResponse(file.file, content_type="text/plain")
            response["Content-Disposition"] = f"attachment; filename={filename}"
            return response
        except Files.DoesNotExist:
            return render(request, "file_transfer_tool/does_not_exist.html")
