#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:18:47 2024

@author: shishira
"""

from paddleocr import PaddleOCR

import warnings
import logging

logging.getLogger('ppocr').setLevel(logging.ERROR)

warnings.filterwarnings("ignore", message="Since the angle classifier is not initialized, it will not be used during the forward process")

ocr_model = PaddleOCR(lang= 'en',use_angle_cls=True)

def puddle_ocr(image):
    full_string = ''
    text = ocr_model.ocr(image)
    t_0 = text[0]
    for t in t_0:
        full_string+=str(t[1][0]) + "  "
    return full_string




