# import detect.py file
from helper_func import Yolov3_model

from flask import Flask, redirect, url_for, render_template, jsonify, request, make_response, Response
from werkzeug.utils import secure_filename

import argparse
import time
import os

#import binascii
import base64
import io
import json

app = Flask(__name__)

# LOAD YOLOV3 MODEL WITH COCO DATASET
baseYolov3 = Yolov3_model(labelsPath = "static/yolov3/coco.names",
                          wpath = "static/yolov3/yolov3.weights",
                          cfgpath = "static/yolov3/yolov3.cfg")
# load model and store in baseYolov3.nets
baseYolov3.loadModel()

# LOAD YOLOV3 MODEL WITH CUSTOM DATASET
customYolov3 = Yolov3_model(labelsPath="static/yolov3_custom/obj.names",
                          wpath = "static/yolov3_custom/yolov3-custom_final.weights",
                          cfgpath = "static/yolov3_custom/yolov3-custom-test.cfg")
# load model and store in baseYolov3.nets
customYolov3.loadModel()

# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template("pages/index.html", title="Home page")

# Yolov3 base route
@app.route('/yolov3', methods=['GET'])
def yolov3():
    return render_template("pages/yolov3_base.html", title="Yolov3 base")


UPLOAD_PATH = 'static/uploads/'
# Upload image route
@app.route('/_upload-image/', methods=['POST'])
def upload_image():
    is_custom = int(request.form['is_custom'])
    # GET REQUEST IMAGE & STORE ORIGIN IMAGE TO SERVER
    file = request.files['image']
    file_name = ''
    if file:
        file_name = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_PATH + file_name))
    else:
        return  make_response(jsonify(msg='Upload error: image not found!!!'),400)
    origin_url = os.path.join(UPLOAD_PATH + file_name)


    # USING CUSTOM YOLOv3 
    # FROM MY CUSTOM DATASET TO PREDICT
    predict_url = ''
    confidence = []
    classes = []
    if is_custom:
        predict_url, confidences, classes = customYolov3.predictObj(origin_url=origin_url,
                                                                   file_name=file_name,
                                                                   UPLOAD_PATH=UPLOAD_PATH)
    # USING BASE YOLOv3 WITH 80 CLASSES 
    # FROM COCO DATASET TO PREDICT
    else:
        predict_url, confidences, classes= baseYolov3.predictObj(origin_url=origin_url,
                                                                   file_name=file_name,
                                                                   UPLOAD_PATH=UPLOAD_PATH)
        
    # Respone data
    predict_data = list(zip(classes,confidences))
    print(f'predict data:\n{predict_data}')
    
    response = {'origin_url': origin_url, 'predict_url': predict_url, 'predict_data': predict_data}
    return Response(json.dumps(response), mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)