import detect

from PIL import Image
import cv2
import numpy as np
import os

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
    
    def predictObj(self, origin_url, file_name, UPLOAD_PATH):
        # open image
        img = Image.open(origin_url)
        npimg=np.array(img)
        image=npimg.copy()
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # predict image
        res, confidences, classes = detect.get_predection(image,self.nets,self.Lables,self.Colors)
        # get class labels from index
        classes = list(map(lambda index: self.Lables[index], classes))

        image=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
        np_img=Image.fromarray(image)
        # save image to server
        file_name = 'custom_predict_' + file_name
        np_img.save(UPLOAD_PATH + file_name)
        # get predict image url
        predict_url = os.path.join(UPLOAD_PATH + file_name)
        
        return predict_url, confidences, classes




