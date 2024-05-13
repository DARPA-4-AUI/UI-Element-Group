from PIL import Image
import os
import requests
import json
if __name__ == '__main__':
    folder_path = './data/test/'
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if not (file.endswith('jpg')):
                continue
            file_path = os.path.join(root, file)
            filename=file.split('.jpg')[0]
            img1 = open(file_path, 'rb')
            with open('./data/ocr_result/'+filename+'.json', 'r', encoding='utf-8') as input_file:
                ocr_data = json.load(input_file)
            file_resq = {
                "file": img1
            }
            ocr_data_json = json.dumps(ocr_data)

            data = {
                "click_x": "307",
                "click_y": "2088",
                "ocr": ocr_data_json
            }

            res = requests.post("http://172.16.108.178:8888/yolo", files=file_resq,data=data)
            print(res.text)
            with open('./result/'+filename + ".json", "w",encoding='utf-8') as f:
                json.dump(res.json(), f, ensure_ascii=False,indent=4)
