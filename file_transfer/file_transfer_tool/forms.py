from django import forms
from file_transfer_tool.models import Files
from file_transfer_tool.utils import generate_unique_id


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = (
            "name",
            "description",
            "file",
            "password",
        )

    def save(self, commit=True):
        self.instance.url = generate_unique_id()
        return super().save()
