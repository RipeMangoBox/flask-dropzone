# app.py

from flask import Flask, render_template
from img_process import get_processed_image_path

app = Flask(__name__)

@app.route('/')
def index():
    # 原始图片的路径
    input_image_path = "static/img.jpg"

    # 处理图片并获取处理后的图片路径
    processed_image_path = get_processed_image_path(input_image_path)

    # 将处理后的图片路径传递给模板
    return render_template('index.html', processed_image_path=processed_image_path)

if __name__ == '__main__':
    app.run(debug=True)
