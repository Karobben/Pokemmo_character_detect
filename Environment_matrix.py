#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',default = "Environment_P")     #输入文件

args = parser.parse_args()
model = args.input

import os
from scipy.misc import imread, imresize, imshow

Environment = INPUT

Env_list = os.listdir(INPUT)


Reuslt =""
for i in Env_list:
    Dir = INPUT +"/"+i
    os.system("./Duplicat_finder.py -o Garbage -i "+Dir)
    Img_list = os.listdir(Dir)
    for image in Img_list:
        img = imread(Dir +"/"+image)
        image = img.ravel()
        Reuslt = i + "\t" + image


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
Eye.Window_fit(Me_cascade)

#Eye.View()
