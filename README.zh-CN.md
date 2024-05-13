## 本项目基于[yolov5](https://github.com/ultralytics/yolov5)实现对于点击相关界面元素的聚合

### 环境部署

Windows/Linux + python版本3.9
```
pip install requirements.txt
```
### 数据准备

/data下创建4个文件夹：images和JPEGImages内为JPG格式的数据集原始图片，Annotations内为标注的xml文件
```
python make_txt.py
python voc_label.py //文件中classes需要替换为标注的类别名称
```
/data下创建自己数据集的yaml文件，可复制coco.yaml并将train、val、test字段修改为上述代码运行后生成的三个文本文件（.txt）的相对路径

### 训练
```
python train.py
```

### 测试检测
```
python detect.py
```
