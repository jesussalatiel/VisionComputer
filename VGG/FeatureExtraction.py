from VGG.VGG16 import modelVGG16
import cv2
import numpy as np
from os.path import exists, abspath, dirname, join
from os import makedirs, listdir
from keras.preprocessing.image import load_img, save_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image
import datetime
from collections import Counter

# CREATE FILES
DATABASE_IMAGES = dirname(abspath(__file__))
DATABASE_IMAGES = join(DATABASE_IMAGES, 'DATABASE')
makedirs(DATABASE_IMAGES, exist_ok=True)
INPUT_DATABASE_IMAGES = join(DATABASE_IMAGES, 'USERS')
makedirs(INPUT_DATABASE_IMAGES, exist_ok=True)
OUTPUT_DATABASE_IMAGES = join(DATABASE_IMAGES, 'UNKNOWN')
makedirs(OUTPUT_DATABASE_IMAGES, exist_ok=True)


# PARAMETERS
XML_HAARCASCADE = './haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(XML_HAARCASCADE)
INPUT_CAMARA = 0
camara = cv2.VideoCapture('./video_1.mp4')

# SAVE FEATURE EXTRACTION OF USERS
USER_EXTRACTION_FEATURE = dict()

# SAVE VALUES USER
TIMES_VALUES_USER = 5
# Average statistic of user per access system susessful
# (20 + 20 + 20)/TIMES_VALUES_USER = BETA
SAVE_DATA_VALUES_USER = []

# LOAD MODEL
model = modelVGG16()

# WINDOWS PARAMETERS
COLOR_LINE_INIT = (0, 255, 255)
COLOR_LINE_ACCESS = (0, 255, 127)
LINE_WEIGHT = 2
TITLE_WINDOWS_MAIN = 'ASISTENTE VIRTUAL'
NAME_BOX_CV2 = 'Invitado'


def processingImage(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def extractFeactureUsers(path_image=INPUT_DATABASE_IMAGES):
    for file in listdir(path_image):
        image, ext = file.split('.')
        path = '{0}\{1}.jpg'.format(path_image, image)
        imgen_iso = processingImage(path)
        USER_EXTRACTION_FEATURE[image] = model.predict(imgen_iso)[0, :]

def extractFeactureInput(detected_face):
    detected_face = cv2.resize(detected_face, (224, 224))
    img_pixels = image.img_to_array(detected_face)
    img_pixels = np.expand_dims(img_pixels, axis=0)
    img_pixels = preprocess_input(img_pixels)

    return model.predict(img_pixels)[0, :]

def distanceEuclidea(i, source_image, representation):
    
    a = np.matmul(np.transpose(source_image), representation)
    b = np.sum(np.multiply(source_image, source_image))
    c = np.sum(np.multiply(representation, representation))

    return float(round(np.subtract(1, np.divide(a, np.multiply(np.sqrt(b), np.sqrt(c)))), 2))
    
def comparateImages(source_image=None, BETA= 0.20):
    person_name = NAME_BOX_CV2
    value_person = -1
    for i, (name, features) in enumerate(USER_EXTRACTION_FEATURE.items()):
        value = (distanceEuclidea(i, source_image, features))
        if (value < BETA):
            person_name = name
            value_person= value

    return person_name, value_person

def saveImages(source_image):
    image = cv2.resize(source_image, (224, 224))
    date = datetime.datetime.now()
    name = str(date).split('.')[1]
    #cv2.imwrite('{}/{}.jpg'.format(OUTPUT_DATABASE_IMAGES, name), source_image)
    return COLOR_LINE_INIT

def verifyAccess(name, value, image):
        if value == -1:
                return saveImages(image)
        else:
                return COLOR_LINE_ACCESS


extractFeactureUsers()
while(True):
    _, img = camara.read()
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        face = img[int(y):int(y+h), int(x):int(x+w)]
        source_image = extractFeactureInput(face)
        name, value = comparateImages(source_image)

        COLOR = verifyAccess(name, value, face)
        
        cv2.rectangle(img, (x, y), (x+w, y+h), COLOR, LINE_WEIGHT)
        cv2.putText(img, name, (int(x+w-140), int(y-10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, COLOR, LINE_WEIGHT)

    cv2.imshow(TITLE_WINDOWS_MAIN, img)
    # Push 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        USER_EXTRACTION_FEATURE.clear()
        SAVE_DATA_VALUES_USER.clear()
        break
