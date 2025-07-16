import cv2
import numpy as np
import face_recognition
import os

path = 'ImgAttendences'
images = []

classNames = []
myList = os.listdir(path)
print(myList)
# uses the names and import the images one by one
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    #removes the file type and just displays the names
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

#
