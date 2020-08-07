
# Pistol Detector run on Flask server

> Model was trained on Google Colab

> [Link](https://colab.research.google.com/drive/1tsi6OPPe5Rynx6EHK25cipytNhdbHHs5?usp=sharing)

> Dataset: 3000 pistol images

> [Raw dataset](http://www.mediafire.com/file/pvfircmboaelkxc/Gun_data_labeled.zip/file)

## Table of Contents

- [Installing & Running App Locally](#installing--running-app-locally)
- [Deploying on Heroku](#deploying-on-heroku)

## Installing & Running App Locally

> download weights
[./static/yolov3/yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
[./static/yolov3_custom/yolov3-custom_final.weights](https://drive.google.com/file/d/1-1odPhkfyL_yaZMJDCkIPqXNtasj-wBF/view)

> install packages in requirements.txt first

```shell
$ pip install -r requirements.txt
```

> run flask app.
> it will run on http://localhost:5000/ by default

```shell
$ flask run
```

> video demo
[![Demo](https://j.gifs.com/yognWV.gif)](https://www.youtube.com/watch?v=I7nvs4nHoQQ)


## Deploying on Heroku

> updating...
