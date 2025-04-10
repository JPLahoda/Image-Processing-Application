from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='original/')
    processed_image = models.ImageField(upload_to='processed/', null=True, blank=True)
    filter_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image {self.id} - {self.filter_type}"