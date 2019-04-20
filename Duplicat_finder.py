#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-O','--range')   #输入文件
parser.add_argument('-d','-D','--diff',default =0.1,type=float)   #输入文件

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.range
Diff = args.diff

import numpy as np
import matplotlib.pyplot as plt
import itertools

from scipy.misc import imread, imresize, imshow
import cv2
import os
import time
from hashlib import md5
import scipy


image_files = os.popen("ls "+INPUT+"/*").read().split("\n")[:-1]
print(len(image_files))

def img_gray(image):
    image = imread(image)
    return image

def resize(image, height=30, width=30):
    row_res = cv2.resize(image,(height, width), interpolation = cv2.INTER_AREA).flatten()
    col_res = cv2.resize(image,(height, width), interpolation = cv2.INTER_AREA).flatten('F')
    return row_res, col_res


def intensity_diff(row_res, col_res):
    difference_row = np.diff(row_res)
    difference_col = np.diff(col_res)
    difference_row = difference_row > 0
    difference_col = difference_col > 0
    return np.vstack((difference_row, difference_col)).flatten()

def difference_score(image, height = 30, width = 30):
    gray = img_gray(image)
    row_res, col_res = resize(gray, height, width)
    difference = intensity_diff(row_res, col_res)
    return difference

def hamming_distance(image, image2):
    score =scipy.spatial.distance.hamming(image, image2)
    return score

def difference_score_dict(image_list):
    ds_dict = {}
    duplicates = []
    for image in image_list:
        ds = difference_score(image)
        if image not in ds_dict:
            ds_dict[image] = ds
        else:
            duplicates.append((image, ds_dict[image]) )
    return  duplicates, ds_dict

duplicates, ds_dict =difference_score_dict(image_files)
DU_file = []
for k1,k2 in itertools.combinations(ds_dict, 2):
    if hamming_distance(ds_dict[k1], ds_dict[k2])< Diff:
        duplicates.append((k1,k2))
        DU_file.append(k2)

print(len(duplicates))
DU_file =list(dict.fromkeys(DU_file))
print(len(DU_file))

for i in DU_file:
    os.system("mv "+i+" "+OUTPUT+"/")
