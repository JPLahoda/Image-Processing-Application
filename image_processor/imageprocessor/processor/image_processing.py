import os
from datetime import datetime
from io import BytesIO

import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps

from django.core.files.base import ContentFile

def apply_filter(image_path, filter_type):
    img = Image.open(image_path)
    
    if filter_type == 'gray':
        # Convert to grayscale
        processed_img = img.convert('L')
    elif filter_type == 'sepia':
        # Apply sepia filter
        img = img.convert('RGB')
        data = np.array(img)
        sepia_filter = np.array([
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131]
        ])
        processed_data = np.dot(data, sepia_filter.T)
        processed_data[np.where(processed_data > 255)] = 255
        processed_img = Image.fromarray(processed_data.astype('uint8'))
    elif filter_type == 'blur':
        # Apply blur filter
        processed_img = img.filter(ImageFilter.BLUR)
    elif filter_type == 'edge':
        # Edge detection
        img = img.convert('L')
        data = np.array(img)
        processed_data = cv2.Canny(data, 100, 200)
        processed_img = Image.fromarray(processed_data)
    elif filter_type == 'poster':
        # Posterize
        processed_img = img.convert('P', palette=Image.ADAPTIVE, colors=8)
    elif filter_type == 'solar':
        # Solarize
        processed_img = ImageOps.solarize(img, threshold=128)
    else:
        processed_img = img
    
    return processed_img
