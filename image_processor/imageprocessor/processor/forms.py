from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    FILTER_CHOICES = [
        ('gray', 'Grayscale'),
        ('sepia', 'Sepia'),
        ('blur', 'Blur'),
        ('edge', 'Edge Detection'),
        ('poster', 'Posterize'),
        ('solar', 'Solarize'),
    ]
    
    filter_type = forms.ChoiceField(choices=FILTER_CHOICES)
    
    class Meta:
        model = Image
        fields = ['original_image', 'filter_type']