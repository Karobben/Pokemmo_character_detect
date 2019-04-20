from Xlib import display, X
from PIL import Image
import numpy as np
import time
import cv2
import os

import Move
import Brain


Battle_detact = cv2.CascadeClassifier("Battel/Model/cascade.xmld")

'''
I want to see
'''
dir_path = os.path.dirname(os.path.realpath(__file__))

def Region():
    W,H = 1400,800
    dsp = display.Display()
    root = dsp.screen().root
    raw = root.get_image(2140, 100, W,H, X.ZPixmap, 0xffffffff)
    image = Image.frombytes("RGB", (W, H), raw.data, "raw", "RGBX")
    return image


def Window_fit():
    font = cv2.FONT_HERSHEY_SIMPLEX # for text
    '''
    time_A= time.time()
    Moving = "Moving: Unknow"

    image=Region()
    source = image.split()
    Pic_A = np.array(source[0].point(lambda i: i < 70 and 255))
    '''


    Battel_inf = "Battel: No"
    while True:
        #Move.run(1)
        image=Region()
        npimage = np.array(image)
        source = image.split()
        R, G, B = 0, 1, 2
        img1 = source[R].point(lambda i: i < 70 and 255)
        #img_moving = np.array(img1)
        img1 = np.array(img1)[280:400,0:700]
        #cv2.imshow('image1',img1)
        img2 = source[G].point(lambda i: i < 2 and 255)
        img2 = np.array(img2)
        #cv2.imshow('image2',img2) # for ME
        #img3 = source[B].point(lambda i: i < 2 and 255)
        #img3 = np.array(img3)
        #cv2.imshow('image3',img3)

        #time_A = Move.Moving(time_A)

        WhereI = Brain.circal_ME(img2,npimage)
        '''
        if WhereI != "True":
            print("B detect")
            Battel_inf = Battle_detact.detectMultiScale(npimage[:,:,0], 8, 8)
            if Battel_inf != ():
                Battel_inf = "Battel: Yes"
                #Move.Battle_go()
                #cv2.imwrite("tmp/No_Battel_"+str(time.time())+".png",Pic_B)
            else:
                Battel_inf = "Battel: No"
            #cv2.imwrite("Environment_P/Battel/Battel_"+str(time.time())+".png",Pic_B)
        '''
        cv2.putText(npimage,Battel_inf,(1,20), font, 0.5,(255,51,51),2,cv2.LINE_AA)
        cv2.putText(npimage,"Find Me: "+ WhereI,(1,40), font, 0.5,(255,51,51),2,cv2.LINE_AA)
        #cv2.putText(npimage,"Moving: "+ Move_infr,(1,60), font, 0.5,(255,51,51),2,cv2.LINE_AA)
        #cv2.putText(npimage,Moving,(1,40), font, 0.5,(255,51,51),2,cv2.LINE_AA)
        cv2.imshow('image',npimage)
        #cv2.imwrite(dir_path+"/Me/Me"+str(time.time())+".png",img)
        #cv2.imwrite(dir_path+"/Battel/Batte_"+str(time.time())+".png",img_T)
        #take_pic_auto(npimage)
        key = cv2.waitKey(33)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        if key == ord('s'):
            cv2.imwrite(dir_path+"/tmp2/NoP_"+str(time.time())+".png",img_T)
