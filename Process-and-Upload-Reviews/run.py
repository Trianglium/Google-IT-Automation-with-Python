#! /usr/bin/env python3
import os
import requests

# Example External IP Address
external_IP_Address = 12.345.678.90

# Enter your website's exdternal IP Address or your django website's URL
company_url = "http://{}/feedback/".format(External_IP_Address)

# Identify Path of Review (Text) files
feedback_path = "/Process-and-Upload-Reviews/feedback/"
# Get the names of all of the Review files that are avaialble in the Directory 
feedback_dir = os.listdir(feedback_path)

for files in feedback_dir:
    # Go through each text file, reformat them, and post them to the company's website.
    with open(feedback_path+files, 'r') as fb:
        input_sections = fb.read().split('\n')
        customer_reviews = {"title":input_sections[0], "name":input_sections[1], "date":input_sections[2], "comment":input_sections[3]}
        post_action = requests.post(company_url, json=customer_reviews)
        fb.close()
        
        
