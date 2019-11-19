from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import base64
import os

from human_detection_engine import DetectorAPI

tmp_dir = 'tmp'
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

app = Flask(__name__)
odapi = DetectorAPI()


@app.route('/cropping_tool')
def upload_app():
    return render_template('cropping_tool.html')


@app.route('/crop', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filepath = os.path.join(tmp_dir, secure_filename(f.filename))
        f.save(filepath)

        img = odapi.load_img(filepath)
        os.remove(filepath)

        buffer = odapi.encode_img(img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        box, score = odapi.process(img)
        img_cropped, box_cropped = odapi.crop(img, box,
                                              margin_w=int(request.form['margin_w']),
                                              margin_h=int(request.form['margin_h']))
        buffer_cropped = odapi.encode_img(img_cropped)
        img_cropped_base64 = base64.b64encode(buffer_cropped).decode('utf-8')

        return render_template('outcome.html', image_cropped=img_cropped_base64, image=img_base64)


if __name__ == '__main__':
    app.run(debug=True)
