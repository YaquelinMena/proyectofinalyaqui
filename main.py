import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    #Aqui va su código

    img = cv.imread('RX.jpg',0)
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh2 = cv.threshold(thresh1,127,255,cv.THRESH_TRUNC)
    ret,thresh3 = cv.threshold(thresh2,127,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(thresh3,127,255,cv.THRESH_TRUNC)
    ret,thresh5 = cv.threshold(thresh4,127,255,cv.THRESH_TRUNC)
    ret,thresh6 = cv.threshold(thresh5,127,255,cv.THRESH_TRUNC)
    ret,thresh7 = cv.threshold(thresh6,127,255,cv.THRESH_TRUNC)
    ret,thresh8 = cv.threshold(thresh7,127,255,cv.THRESH_TRUNC)
    ret,thresh9 = cv.threshold(thresh8,127,255,cv.THRESH_TRUNC)
    ret,thresh10 = cv.threshold(thresh9,127,255,cv.THRESH_TRUNC)
    ret,thresh11 = cv.threshold(thresh10,127,255,cv.THRESH_TRUNC)
    ret,thresh12 = cv.threshold(thresh11,127,255,cv.THRESH_TRUNC)
    ret,thresh13 = cv.threshold(thresh12,127,255,cv.THRESH_TRUNC)
    ret,thresh14 = cv.threshold(thresh13,127,255,cv.THRESH_TRUNC)
    ret,thresh15 = cv.threshold(thresh14,127,255,cv.THRESH_TRUNC)
    ret,thresh16 = cv.threshold(thresh15,127,255,cv.THRESH_TRUNC)
    ret,thresh17 = cv.threshold(thresh16,127,255,cv.THRESH_TRUNC)
    ret,thresh18 = cv.threshold(thresh17,127,255,cv.THRESH_TRUNC)
    ret,thresh19 = cv.threshold(thresh18,127,255,cv.THRESH_TRUNC)
    ret,thresh20 = cv.threshold(thresh19,127,255,cv.THRESH_TRUNC)
    ret, thresh21 = cv.threshold(thresh20, 127, 255, cv.THRESH_TRUNC)
    ret, thresh22 = cv.threshold(thresh21, 127, 255, cv.THRESH_TRUNC)
    ret, thresh23 = cv.threshold(thresh22, 127, 255, cv.THRESH_TRUNC)
    ret, thresh24 = cv.threshold(thresh23, 127, 255, cv.THRESH_TRUNC)
    ret, thresh25 = cv.threshold(thresh24, 127, 255, cv.THRESH_TRUNC)
    ret, thresh26 = cv.threshold(thresh25, 127, 255, cv.THRESH_TRUNC)
    ret, thresh27 = cv.threshold(thresh26, 127, 255, cv.THRESH_TRUNC)
    ret, thresh28 = cv.threshold(thresh27, 127, 255, cv.THRESH_TRUNC)
    ret, thresh29 = cv.threshold(thresh28, 127, 255, cv.THRESH_TRUNC)
    ret, thresh30 = cv.threshold(thresh29, 127, 255, cv.THRESH_TRUNC)
    ret, thresh31 = cv.threshold(thresh30, 127, 255, cv.THRESH_TRUNC)
    ret, thresh32 = cv.threshold(thresh31, 127, 255, cv.THRESH_TRUNC)
    ret, thresh33 = cv.threshold(thresh32, 127, 255, cv.THRESH_TRUNC)
    ret, thresh34 = cv.threshold(thresh33, 127, 255, cv.THRESH_TRUNC)
    ret, thresh35 = cv.threshold(thresh34, 127, 255, cv.THRESH_TRUNC)

    titles = ['Original Image','Figura 1']
    images = [img, thresh35]
    for i in range(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

    return thresh35