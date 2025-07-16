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

# Find the encoding for each one of the images:

def find_encodings(images):
    encode_list = []
    for img in images:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)

    return encode_list

encodeListKnown = find_encodings(images)
print(len(encodeListKnown))

# faceLoc = face_recognition.face_locations(imgTrump)[0]
# encodeTrump = face_recognition.face_encodings(imgTrump)[0]
# cv2.rectangle(imgTrump,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255, 0, 255),2)

# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255, 0, 255),2)

# results = face_recognition.compare_faces([encodeTrump],encodeTest)
# #find the distance
# #lower the distance the better match is
# faceDis = face_recognition.face_distance([encodeTrump], encodeTest)

