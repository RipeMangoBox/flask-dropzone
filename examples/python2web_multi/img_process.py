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

def replace_last_folder(path, new_folder_name):
    # 替换路径中的最后一级目录
    head, tail = os.path.split(path)
    new_path = os.path.join(head, new_folder_name)
    return new_path

def get_processed_image_path(input_path):
    # 获取目录路径和文件名
    directory_path = os.path.dirname(input_path)
    filename = os.path.basename(input_path)

    # 替换路径中的最后一级目录
    processed_image_paths = replace_last_folder(directory_path, 'processed_images')

    # 保存处理后的图片的路径
    output_path = os.path.join(processed_image_paths, "processed_" + filename)
    print(f"output_path: {output_path}")

    # 进行图片处理的代码
    process_image(input_path, output_path)

    return output_path
