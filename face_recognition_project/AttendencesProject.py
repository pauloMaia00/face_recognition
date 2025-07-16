import cv2
import numpy as np
import face_recognition
import os

path = 'ImgAttendances'
images = []

classNames = []
myList = os.listdir(path)
print(myList)

imgTrump = face_recognition.load_image_file('ImageBasic/45_donald_trump_w-1250.jpg')
imgTrump = cv2.cvtColor(imgTrump,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/trump.jpg')
#imgTest = face_recognition.load_image_file('ImageBasic/bill_clinton.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

