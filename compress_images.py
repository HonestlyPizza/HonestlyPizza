# -*- coding: utf-8 -*-
from PIL import Image
import os
import sys

os.chdir(r"c:\Users\jonah\Important\Random\Readme\HonestlyPizza")

# Image compression script
image_dir = r"images\caeb"
original_dir = os.path.join(image_dir, "original")

images = [
    "Thumbnail1.png",
    "Thumbnail2.png", 
    "Thumbnail3.png",
    "Thumbnail4.png"
]

total_before = 0
total_after = 0

for img_name in images:
    original_path = os.path.join(original_dir, img_name)
    output_path = os.path.join(image_dir, img_name)
    
    if os.path.exists(original_path):
        print(f"Compressing {img_name}...")
        
        # Open image
        img = Image.open(original_path)
        
        # Get original size
        orig_size = os.path.getsize(original_path) / (1024 * 1024)
        total_before += orig_size
        
        # Resize if too large (max 1920x1080)
        img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
        
        # Save with compression
        img.save(output_path, "PNG", optimize=True, quality=85)
        
        # Get new size
        new_size = os.path.getsize(output_path) / (1024 * 1024)
        total_after += new_size
        reduction = (1 - new_size / orig_size) * 100
        
        print(f"  {img_name}: {orig_size:.1f}MB -> {new_size:.1f}MB ({reduction:.1f}% reduction)")

print(f"\nTotal: {total_before:.1f}MB -> {total_after:.1f}MB ({(1 - total_after/total_before)*100:.1f}% reduction)")
