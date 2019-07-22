import cv2
import numpy as np

# PARAMETERS
XML_HAARCASCADE = '../haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(XML_HAARCASCADE)
INPUT_CAMARA = 0
#camara = cv2.VideoCapture('BASE DE DATOS USUARIOS.jpg')

# WINDOWS PARAMETERS
COLOR_LINE_INIT = (0, 255, 255)
COLOR_LINE_ACCESS = (0, 255, 127)
LINE_WEIGHT = 2
TITLE_WINDOWS_MAIN = 'ASISTENTE VIRTUAL'
NAME_BOX_CV2 = 'Invitado'

#while(True):
img = cv2.imread('BASE DE DATOS USUARIOS.jpg')
faces = face_cascade.detectMultiScale(img, 1.3, 5)
for i, (x, y, w, h) in enumerate(faces):
    face = img[int(y):int(y+h), int(x):int(x+w)]
    cv2.rectangle(img, (x, y), (x+w, y+h), COLOR_LINE_INIT, LINE_WEIGHT)
    cv2.imwrite('imagen_{0}.jpg'.format(i), face)
        
cv2.imshow(TITLE_WINDOWS_MAIN, img)
cv2.waitKey(0)
    # Push 'q' to exit
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
