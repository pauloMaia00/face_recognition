import cv2
import numpy as np
import face_recognition

imgTrump = face_recognition.load_image_file('ImageBasic/45_donald_trump_w-1250.jpg')
imgTrump = cv2.cvtColor(imgTrump,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/trump.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgTrump)[0]
encodeTrump = face_recognition.face_encodings(imgTrump)[0]
cv2.rectangle(imgTrump,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255, 0, 255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTrumpTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255, 0, 255),2)

cv2.imshow('Donald Trump', imgTrump)
cv2.imshow('Donald Test', imgTest)
cv2.waitKey(0)