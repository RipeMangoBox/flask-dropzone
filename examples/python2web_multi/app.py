# app.py

import os
from flask import Flask, render_template
import cv2
import shutil

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def get_image_list(folder_path):
    # 获取文件夹内所有图像文件的路径
    image_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    print(f'image_list: {image_list}')
    return image_list


@app.route('/multiple_images')
def multiple_images():
    img1 = "static/raw_images/img1.jpg"
    img2 = "static/raw_images/img2.jpg"
    img3 = "static/raw_images/img3.jpg"
    img4 = '/home/ripemangobox/Coding/wsl2-Homework/Undergraduate_FirstYear/Information_Retrival/reverse_image_search/train/Bouvier_des_Flandres/n02106382_6290.JPEG'
    
    original_path = '/home/ripemangobox/Coding/wsl2-Homework/Undergraduate_FirstYear/Information_Retrival/reverse_image_search/test/bannister/n02788148_47071.JPEG'

    # 获取当前工作目录
    current_directory = os.getcwd()
    print(f'current_directory: {current_directory}')

    # 构建目标路径，即当前工作目录下的相同文件名
    destination_path = os.path.join(current_directory, 'static/raw_images/img5.jpg')
    # destination_path='static/raw_images/img5.jpg'

    img5 = destination_path
    # 使用shutil复制文件
    shutil.copy2(original_path, destination_path)

    return render_template('multiple_images.html', 
                           img1=img1, img2=img2, img3=img3,img4=img4, img5=img1, 
                           img6=img2, img7=img3,img8=img1,img9=img1, img10=img2)


# @app.route('/')
# def index():
#     # 图片文件夹的路径
#     image_folder_path = basedir
#     image_folder_path = "static/raw_images"
    
#     # 获取文件夹内所有图像文件的路径
#     image_list = get_image_list(image_folder_path)

#     # 处理每个图像并获取处理后的图片路径列表
#     processed_image_paths = [get_processed_image_path(image_path) for image_path in image_list]

#     print(f'processed_image_paths: {processed_image_paths}')
    
#     # 将处理后的图片路径列表传递给模板
#     return render_template('index.html', processed_image_paths=processed_image_paths)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
