from django import forms

from .models import StatusModel


class StatusModelForm(forms.ModelForm):

    class Meta:
        model = StatusModel
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if len(content) > 250:
            raise forms.ValidationError(
                "Length of the content cannot be more than 250 words")

        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image")

        if content is None and image is None:
            raise forms.ValidationError("Content/Image field is required")

        return super().clean(*args, **kwargs)
