# image_processing.py
from PIL import Image
from flask import send_file

def process_image(input_path, output_path):
    # 进行图片处理的代码，例如使用PIL库
    image = Image.open(input_path)
    # 在这里可以添加你的图片处理逻辑

    # 保存处理后的图片
    image.save(output_path)

def get_processed_image_path(input_path):
    output_path = "static/processed_image.jpg"  # 保存处理后的图片的路径
    process_image(input_path, output_path)
    return output_path
