#! /usr/bin/env python3
import os
import requests

url = 'http://'+'[external IP Address]'+'/fruits/'
fruit_path = "supplier-data/descriptions/"
fruit_dir = os.listdir(fruit_path)
catalog = {}
for files in fruit_dir:
    with open(str(fruit_path+files), 'r') as f:
        entry = f.read().split('\n')
        catalog["name"] = entry[0]
        weight = entry[1].split(' ')
        catalog["weight"] = weight[0]
        catalog["description"] = entry[2]
        item_num = os.path.splitext(files)[0]
        catalog["image_name"] = item_num + '.jpeg'
        post_entry = requests.post(url, json=catalog)
