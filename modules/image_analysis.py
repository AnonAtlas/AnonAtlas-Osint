# image_analysis.py
import exiftool
import os

def analyze_image(image_path):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(image_path)
    return metadata