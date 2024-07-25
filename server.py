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


app = FastAPI()

@app.get('/')
def test():
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    return {"message":"sucess"}


@app.post('/upload_file')
def image_upload(file:UploadFile):
   with open('./temp/temp.jpeg','wb') as f:
       f.write(file.file.read())
   data = puddle_ocr('./temp/temp.jpeg') 
   return groq_api_response(data)
  
  
