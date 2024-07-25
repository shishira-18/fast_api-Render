#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:18:47 2024

@author: shishira
"""

from paddleocr import PaddleOCR
ocr_model = PaddleOCR(
        lang='en',
                  drop_score=0,
                  use_angle_cls=False,
                  cls=False,
                  rec_model_dir='paddle_files/default/rec/en/en_PP-OCRv3_rec_infer',
                  det_model_dir='paddle_files/default/det/en/en_PP-OCRv3_det_infer',
                  cls_model_dir='paddle_files/default/cls/ch_ppocr_mobile_v2.0_cls_infer',
                  det_db_box_thresh=0.3,
                  enable_mkldnn=True,
                  use_gpu=False
        
        
        
    )


def puddle_ocr(image):

    full_string = ''
    text = ocr_model.ocr(image)
    t_0 = text[0]
    for t in t_0:
        full_string+=str(t[1][0]) + "  "
    return full_string




