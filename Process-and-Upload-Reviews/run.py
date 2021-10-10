#! /usr/bin/env python3
import os
import requests

url = 'http://130.211.204.15/feedback/'

fb_path = "/data/feedback/"
fb_dir = os.listdir(fb_path)
feedback = {}
for files in fb_dir:
    with open(str(fb_path+files), 'r') as fb:
        fb_sections = fb.read().split('\n')
        feedback["title"] = fb_sections[0]
        feedback["name"] = fb_sections[1]
        feedback["date"] = fb_sections[2]
        feedback["comment"] = fb_sections[3]
        post_action = requests.post(url, json=feedback)
