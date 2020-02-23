from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import DownloadForm, UploadFileForm
from .models import Files


class Upload(FormView):
    template_name = "file_transfer_tool/upload.html"
    form_class = UploadFileForm

    def form_valid(self, form: UploadFileForm) -> HttpResponse:
        file = form.save(commit=True)
        download_url = f"{self.request.get_host()}/download/{file.id}/"
        return render(
            request=self.request,
            template_name="file_transfer_tool/successful_upload.html",
            context={"file": file, "download_url": download_url},
        )


class Download(FormView):
    template_name = "file_transfer_tool/download_password.html"
    form_class = DownloadForm

    def _file_exists(self) -> bool:
        try:
            Files.objects.get(id=self.kwargs.get("id"))
            return True
        except (Files.DoesNotExist, ValidationError):
            return False

    def form_valid(self, form: DownloadForm) -> HttpResponse:
        """
        Only allows downloading if the correct password had been given
        """
        given_password = form["password"].value()
        file = Files.objects.get(id=self.kwargs.get("id"))
        if file.password != given_password:
            return HttpResponse("Invalid password was parsed", status=401)
        filename = file.file.name.split("/")[-1]
        response = HttpResponse(file.file, content_type="text/plain")
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not self._file_exists():
            return render(
                request=request,
                template_name="file_transfer_tool/does_not_exist.html",
                context={"object_identity": self.kwargs.get("id")},
                status=404,
            )
        return super().get(request, *args, **kwargs)
