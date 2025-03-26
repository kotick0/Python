import os
import cv2 as cv 
import numpy as np

#Get folder names from directory
people = []
for i in os.listdir(r'train/'):
    people.append(i)

#Set root directory & import haar alghoritm
DIR = r'/home/kotik2137/github/python-opencv-tests/Face_Recognition/train'
haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []

# Add per person subfolder to directory 
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

# Add img specific to path var (rootDir/subDir/img)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
# Let OpenCV read the image from path & grayscale
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
# Haar face detection & draw a rectangle
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                # Set variable face roi (Region of interest) / Crop the image
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training done!")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training the recognizer on features list and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

