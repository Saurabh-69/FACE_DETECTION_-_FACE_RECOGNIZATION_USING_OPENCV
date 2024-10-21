import os
import cv2
import numpy as np


haar_cascade = cv2.CascadeClassifier(r"C:\Users\saurabh.kale\Downloads\SQL_QUERY_GENERATOR_TWO\SQL_QUERY_GENERATOR\SQL_QUERY_GENERATOR\haar_face.xml")
DIR = r'C:\Users\saurabh.kale\Downloads\SQL_QUERY_GENERATOR_TWO\SQL_QUERY_GENERATOR\SQL_QUERY_GENERATOR\Faces'
people = ['Elon', 'Sam', 'Bill', 'Satya']

features = []
labels = []
 
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)
create_train()
print("TRAINING DONE ")
# print(f'Length of features = {len(features)}')
# print(f'Length of label = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer =  cv2.face.LBPHFaceRecognizer_create()

# TRAIN THE RECOGNIZER ON THE FEATURE LIST AND LABELS LIST
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
