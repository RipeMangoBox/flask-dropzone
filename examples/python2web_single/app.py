# app.py

import os
from flask import Flask, render_template
from img_process import get_processed_image_path
import cv2
import numpy as np

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def img_copy2local(original_path, destination_path):
    img=cv2.imread(original_path)
    cv2.imwrite(destination_path, img)

@app.route('/')
def index():
    print(f'basedir: {basedir}')
          
    # 图片文件夹的路径
    input_image_path = basedir + "/static/raw_images/img.jpg"
    input_image_path = "static/raw_images/img.jpg"

    print(f'input_image_path: \t\t{input_image_path}')

    # processed_image_path = get_processed_image_path(input_image_path)
    processed_image_path = "/home/ripemangobox/Coding/Github/flask-dropzone/examples/python2web_single/static/raw_images/n02727426_4398.JPEG"
    path = "static/result_images/img2.jpg"

    img_copy2local(processed_image_path, path)

    # 将处理后的图片路径列表传递给模板
    return render_template('index.html', processed_image_path=path)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
