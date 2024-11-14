## The project aggregates click-related interface elements based on [yolov5](https://github.com/ultralytics/yolov5)

### Environment Setup

Windows/Linux + python version 3.9

```
pip install requirements.txt
```

### Data Preparation

Create 4 folders under /data：images and JPEGImages containing raw dataset images in JPG format, Annotations containing annotated xml files.

```
python make_txt.py
python voc_label.py //Replace classes in the file with the names of annotated classes
```

Create a yaml file for your dataset in /data, you can copy coco.yaml and modify the train, val, test fields to the relative paths of the three text files (.txt) generated after running the above code.

### Training

```
python train.py
```

Our training subset is located in /label_data_org.

### Test Detection

```
python detect.py
```

