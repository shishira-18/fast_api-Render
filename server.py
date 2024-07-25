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

app = FastAPI()

@app.get('/')
def test():
    
    return json.loads(groq_api_response("sathish"))


@app.post('/upload_file')
async def image_upload(file:UploadFile):
   with open('./temp/temp.jpeg','wb') as f:
       f.write(file.file.read())
   data = puddle_ocr('./temp/temp.jpeg') 
   response =  await json.loads(groq_api_response(data))
   return response
