import cv2
import time

from scipy.misc import imread, imresize, imshow
from hashlib import md5
import scipy
import numpy as np
import time
import cv2
import os

Me_cascade = cv2.CascadeClassifier("Model_test/cascade.xml")
Battle_detact = cv2.CascadeClassifier("Battel/Model2/cascade.xml")


def circal_ME(img2,npimage):
    WhereI = Me_cascade.detectMultiScale(img2, 6, 6)
    Result = "False"
    if WhereI != ():
        #print(WhereI)
        #for (x,y,w,h) in WhereI:
        #    cv2.rectangle(npimage,(x,y),(x+w,y+h),(255,0,255),2)
        for i in WhereI:
            if i[3] > 20:
                #print(i)
                (x,y,w,h) =i
                cv2.rectangle(npimage,(x,y),(x+w,y+h),(0,255,255),2)
                #print(iq)
        for i in WhereI:
            x = i[0]
            y = i[1]
            if x<= 305 and x >= 180 and y >= 15 and y <= 200:
                Result = "True"
                #if w == 120:
                    #if x> 360 or x < 180 or y < 15 or y > 200:
                        #img_T =Region_c()[:,:,0][y:y+w,x:x+w]
                        #cv2.imwrite(dir_path+"/Negtive/Nagtive_"+str(time.time())+".png",img_T)
    return Result

def Battel_det(Battel_inf,npimage):
    pass
import numpy as np
import time
import cv2
import os

def Moving_det(time_A,Pic_A,time_B,Pic_B):
    time_B = time.time()
    Result = "detecting"
    if time_B - time_A > 1:
        time_s = "True"
        time_A =time_B
        Pic_diff = scipy.spatial.distance.hamming(Pic_A.ravel(), Pic_B.ravel())
        if Pic_diff < 0.04:
            Result = "Stopped"
        else:
            Result = "Moving"
            Pic_A = Pic_B
        print(Pic_diff)
    return time_A,Pic_A,Result
