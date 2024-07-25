#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:18:47 2024

@author: shishira
"""

from paddleocr import PaddleOCR




def puddle_ocr(image):
    ocr_model = PaddleOCR(lang= 'en',use_angle_cls=True)
    full_string = ''
    text = ocr_model.ocr(image)
    t_0 = text[0]
    for t in t_0:
        full_string+=str(t[1][0]) + "  "
    return full_string




