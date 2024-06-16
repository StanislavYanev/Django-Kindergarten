from django import forms
from .models import GalleryImage


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'name', 'age', 'group']
