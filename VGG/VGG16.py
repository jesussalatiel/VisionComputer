import tensorflow as tf
from keras.models import Model, Sequential
from keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from os.path import exists, abspath, dirname

#GPU Configuration
from keras import backend as K
a = K.tensorflow_backend._get_available_gpus()

#Verify Weights
VERIFY_WEIGHTS = '{0}\weights_mat_to_keras.h5'.format(dirname(abspath(__file__)))
if exists(VERIFY_WEIGHTS) is False:    
    from .GetWeights import createWeigths
   

def modelVGG16(WEIGHTS=VERIFY_WEIGHTS, SIZE_HEIGHT=224, SIZE_WIDTH=224):
    try:       
        model = Sequential()
        model.add(ZeroPadding2D((1, 1), input_shape=(SIZE_WIDTH, SIZE_HEIGHT, 3)))

        #Bloque 1
        model.add(Convolution2D(64, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        #Bloque 2
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(128, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        #Bloque 3
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        #Bloque 4
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        #Bloque 5
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1, 1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        #Bloque 6
        model.add(Convolution2D(4096, (7, 7), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Convolution2D(4096, (1, 1), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Convolution2D(2622, (1, 1)))
        model.add(Flatten())
        model.add(Activation('softmax'))
        
        vgg_face_descriptor = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)
        
        vgg_face_descriptor.load_weights(WEIGHTS)

    except (ValueError, TypeError) as err:
        print('Error Weights.')
    
    return vgg_face_descriptor

def __init__(self, *args, **kwargs):
    modelVGG16()