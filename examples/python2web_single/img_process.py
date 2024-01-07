# image_processing.py

from PIL import Image
from flask import send_file
import os

def process_image(input_path, output_path):
    # 进行图片处理的代码，例如使用PIL库
    image = Image.open(input_path)
    # 在这里可以添加你的图片处理逻辑

    # 保存处理后的图片
    image.save(output_path)

def get_processed_image_path(input_path):
    # 获取目录路径和文件名
    directory_path = os.path.dirname(input_path)
    filename = os.path.basename(input_path)

    # 保存处理后的图片的路径
    output_path = os.path.join(directory_path, "processed_" + filename)
    # output_path = "static/raw_images/processed_image.jpg"

    print(f"output_path: \t\t{output_path}")

    # 进行图片处理的代码
    process_image(input_path, output_path)

    return output_path
