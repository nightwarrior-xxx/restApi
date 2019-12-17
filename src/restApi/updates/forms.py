from django import forms
from .models import Updates as UpdatesModel

class UpdatesModelForm(forms.ModelForm):
    class Meta:
        model = UpdatesModel
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content")
        if content == "":
            content = None
        image = data.get("image")
        if content is None and image is None:
            raise forms.ValidationError("Content/Image is required.")
        return super().clean(*args, **kwargs)
