# import system module
import sys, socket
from gtts import gTTS
import os
import pyttsx3
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        #self.ui.control_bt.clicked.connect(self.controlTimer)
        self.controlTimer()


    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        
    def close(self):
        print('Cerrar')

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            #self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            #self.ui.control_bt.setText("Start")

    def isInternetUp(self):
        try:
            socket.gethostbyname('google.com')
            conexion = socket.create_connection(('google.com', 80), 1)
            conexion.close()
            return True
        except socket.gaierror:
            return False        

if __name__ == '__main__':

    #app = QApplication(sys.argv)

     # create and show mainWindow
    #mainWindow = MainWindow()

    #print(mainWindow.isInternetUp())    
    #mainWindow.show()
    #sys.exit(app.exec_())
    es_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    
    engine = pyttsx3.init()
    engine.setProperty('voice', es_voice_id)
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 10)
    

    engine.say("¡I love you!")
    engine.runAndWait()
