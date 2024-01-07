# -*- coding: utf-8 -*-
# app.py

import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

from image_processing import get_processed_image_path


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DOWNLOAD_PATH=os.path.join(basedir, 'static'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')

@app.route('/single_image')
def index():
    # 原始图片的路径
    input_image_path = "static/img.jpg"

    # 处理图片并获取处理后的图片路径
    processed_image_path = get_processed_image_path(input_image_path)

    # 将处理后的图片路径传递给模板
    return render_template('single_image.html', processed_image_path=processed_image_path)

@app.route('/multiple_images')
def multiple_images():
    img1 = "static/raw_images/img1.jpg"
    img2 = "static/raw_images/img2.jpg"
    img3 = "static/raw_images/img3.jpg"
    img4 = "static/raw_images/img4.jpg"
    img5 = "static/raw_images/img5.jpg"
    img6 = "static/raw_images/img6.jpg"
    img7 = "static/raw_images/img7.jpg"
    img8 = "static/raw_images/img8.jpg"
    img9 = "static/raw_images/img9.jpg"
    img10 = "static/raw_images/img10.jpg"
    return render_template('multiple_images.html', img1=img1, img2=img2, img3=img3, img4=img4, img5=img5, img6=img6, img7=img7, img8=img8, img9=img9, img10=img10)

if __name__ == '__main__':
    app.run(debug=True, port=4999)
