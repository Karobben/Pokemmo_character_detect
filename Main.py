#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m','-M','--Model')     #输入文件

args = parser.parse_args()
model = args.Model

import time
import Eye
import os
print("Please put the window in the correct place and press \"q\" to start")
import cv2




dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
Eye.Window_fit()

#Eye.View()
