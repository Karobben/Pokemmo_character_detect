#!/usr/bin/env python3

import os , cv2
from PIL import Image
import argparse
import time
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-O','--range')   #输入文件

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.range


A = os.popen("ls "+INPUT+"/*").read().split("\n")[:-1]

Num = 0
for i in A[:3000]:
  Num +=1
  img =np.array(Image.open(i))
  img[140:230,290:380] = img[140:230,190:280]
  cv2.imwrite(OUTPUT+"/Bk_"+str(time.time())+".png",img)
