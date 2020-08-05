import detect

from PIL import Image
import cv2
import numpy as np
import os
import io

import base64


class Yolov3_model:
    # initialize paths
    def __init__(self, labelsPath, wpath, cfgpath):
        self.labelsPath = labelsPath
        self.wpath = wpath
        self.cfgpath = cfgpath

    def loadModel(self):
        self.Lables = detect.get_labels(self.labelsPath)
        self.Colors = detect.get_colors(self.Lables)

        self.Weights = detect.get_weights(self.wpath)

        CFG = detect.get_config(self.cfgpath)
        nets = detect.load_model(CFG, self.Weights)
        
        self.nets = nets
    
    def predictObj(self, cv2img):
        # predict image
        res, confidences, classes = detect.get_predection(cv2img,self.nets,self.Lables,self.Colors)
        # get class labels from index
        classes = list(map(lambda index: self.Lables[index], classes))
        # convert cv2img to binary image
        binimg = cv2img_to_strimg(res)

        return binimg, confidences, classes



### Convert code below base on post "Receive and Send back Image in Flask: In memory solution"
### Link: https://medium.com/csmadeeasy/send-and-receive-images-in-flask-in-memory-solution-21e0319dcc1

# Convert image from byte image to cv2.RGB image
# Input:
#   byte_img : type bytes
# Output:
#   cv2img : type numpy.ndarray
def byteimg_to_cv2img(byte_img):
    npimg = np.fromstring(byte_img, np.uint8)
    cv2img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2img = cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)

    return cv2img

# Convert image from cv2.RGB image to binary image
# Input:
#   cv2img : type numpy.ndarray
# Output:
#   strimg : type string
def cv2img_to_strimg(cv2img):
    np_img = Image.fromarray(cv2img.astype("uint8"))
    raw_bytes = io.BytesIO()
    np_img.save(raw_bytes, "JPEG")
    raw_bytes.seek(0)
    img_base64 = base64.b64encode(raw_bytes.read())
    
    return str(img_base64)


