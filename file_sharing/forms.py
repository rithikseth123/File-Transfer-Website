from django import forms
from .models import SharedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['file', 'expiration_date']
        labels = {
            'file': 'Upload File',
            'expiration_date': 'Valid Date(MM/DD/YYYY)'
        }
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
