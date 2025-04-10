from django.shortcuts import render, redirect
from django.conf import settings
from .models import Image
from .forms import ImageUploadForm
from .image_processing import apply_filter
import os
from datetime import datetime

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            
            # Save original image
            image.save()
            
            # Process image
            original_path = image.original_image.path
            processed_img = apply_filter(original_path, image.filter_type)
            
            # Save processed image
            processed_filename = f"processed_{datetime.now().timestamp()}.jpg"
            processed_path = os.path.join(settings.MEDIA_ROOT, 'processed', processed_filename)
            processed_img.save(processed_path)
            
            # Update model with processed image
            image.processed_image = os.path.join('processed', processed_filename)
            image.save()
            
            return redirect('display_image', image_id=image.id)
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def display_image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'display.html', {'image': image})