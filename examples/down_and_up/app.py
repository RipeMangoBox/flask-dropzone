import uuid
import os
from flask import Flask, render_template, request, send_from_directory, url_for
from flask_dropzone import Dropzone

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

@app.route('/mulfileupload/',methods=['GET','POST'])
def mulfileupload():
    if request.method=='POST':
        files=request.files.getlist('wenjian')
        filelist=[]
        urllist=[]
        for file in files:
            filename=file.filename
            filetype=filename.split('.')[-1]
            print(filename)
            print(filetype)
            uploadpath=os.getcwd()+os.sep+'static/file'
            if not os.path.exists(uploadpath):
                os.mkdir(uploadpath)
            filename=str(uuid.uuid1())+'.'+filetype
            print(filename)
            file.save(uploadpath+os.sep+filename)
            filelist.append(filename)
            #照片回显url
            url = url_for("static", filename="file/" + filename)
            urllist.append(url)
 
        return render_template('index.html',msg='文件上传成功',filelist=filelist,urllist=urllist)
    else:
        return render_template('index.html')
 
@app.route('/down/<filename>/')
def down(filename):
    dir=os.getcwd()+os.sep+'static/file/'
    print(dir+filename)
    #下载图片设置
    return send_from_directory(dir,filename,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
