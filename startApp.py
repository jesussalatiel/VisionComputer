import threading
import os, time

def startEnvironment():
    os.system('activate Asistente')

def startWindows():
    #Esperamos que la Api sea inicializada
    time.sleep(5)
    #Ejecutamos la pantalla principal del software
    os.system('python main_window.py')
    print('Aplicación Iniciada')

def startApi():
    #Ejecutamos la Api Spring Boot
    os.system('python runApi.py')
    print('API funcionando')

if __name__ == '__main__':
    #Definimos los procesos a ejecutar
    anaconda = threading.Thread(target = startEnvironment)
    windows = threading.Thread(target= startWindows)
    api = threading.Thread(target = startApi)

    #Iniciamos los procesos en paralelo
    #anaconda.start()
    #api.start()
    windows.start()

