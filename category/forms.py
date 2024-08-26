from django import forms
from .models import CategoryModel

class BrandForm(forms.ModelForm):
    class Meta:
        model= CategoryModel
        fields='__all__'