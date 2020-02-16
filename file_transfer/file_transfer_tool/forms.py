from django import forms
from file_transfer_tool.models import Files


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = (
            "name",
            "description",
            "file",
            "password",
        )
