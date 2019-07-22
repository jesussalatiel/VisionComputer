import os, requests 
import platform
print("Verificacion del sistema x64")

arquitectura = platform.machine()

if (arquitectura == 'AMD64'):
    #Verificacion de paquetes
    python3 = os.system("python -V")
    conda = os.system("conda -V")
    pip3 = os.system("pip -V")
    mongo = os.system("mongo --version")



else:
    print('No se puede ejecutar el script en la {0} version.'.format(arquitectura))
