#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:07:59 2024

@author: shishira
"""


from fastapi import FastAPI,UploadFile

from image_to_text import puddle_ocr
import sys
from groq_api import  groq_api_response
import json
import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    handlers=[logging.FileHandler('paddleocr_debug.log'), logging.StreamHandler()])

app = FastAPI()

@app.get('/test_json')
def test():
    return json.loads(groq_api_response("sathish"))

@app.post('/test_ocr')
async def test_ocr(file:UploadFile):
    try:
        with open('./temp/temp.jpeg','wb') as f:
            f.write(file.file.read())
        data =  puddle_ocr('./temp/temp.jpeg') 
        logging.debug(f'OCR result: {data}')
        return data
    except Exception as e:
        print(f'error during process:{e}')
        
    
@app.post('/upload_file')
async def image_upload(file:UploadFile):
   with open('./temp/temp.jpeg','wb') as f:
       f.write(file.file.read())
   data = puddle_ocr('./temp/temp.jpeg') 
   response =  await json.loads(groq_api_response(data))
   return response
