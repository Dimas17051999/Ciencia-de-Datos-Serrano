import requests
import time 
import threading
import concurrent.futures
import matplotlib.pyplot as plt 
import numpy as np
##########################################################################################
#####################             ACTIVIDAD 1           ################################# 
#########################################################################################
def descargar_sitio1(url, sesion):
    with sesion.get(url) as respuesta1: 
        print("Leyendo {} de {}".format(len(respuesta1.content), url))

def descargar_todo1(sitios):
    with requests.Session() as sesion:
        for url in sitios: 
            descargar_sitio1(url, sesion)

if __name__ == '__main__':
    sitios =["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
             "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
    #print('Se descargaron {} sitios en {} segundos'.format(len(sitios1), duracion1))
##########################################################################################
#####################             ACTIVIDAD 2           ################################# 
#########################################################################################
thread_local= threading.local()

def get_sesion():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def descargar_sitio2(url):
    sesion2 = get_sesion()
    with sesion2.get(url) as respuesta2:
        print("Leyendo {} de {}".format(len(respuesta2.content), url))
        
def descargar_todo2(sitios):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ejecutor: 
        ejecutor.map(descargar_sitio2, sitios)
        
##########################################################################################
#####################             ACTIVIDAD 3           ################################# 
#########################################################################################

duracion_sincrono = []
for i in range(10):
    tiempo_inicio1= time.time()
    descargar_todo1(sitios)
    duracion_sincrono.append(time.time()-tiempo_inicio1) 

duracion_hilos = []
for m in range(10):
    tiempo_inicio2= time.time()
    descargar_todo2(sitios)
    duracion_hilos.append(time.time()-tiempo_inicio2) 

print(duracion_hilos)
print(duracion_sincrono)
np.mean(duracion_hilos)
np.mean(duracion_sincrono)
tiempos = [duracion_sincrono, duracion_hilos]
plt.boxplot(tiempos, patch_artist= True)
plt.xticks([1,2], ["Concurencia sincrona", "Concurrencia hilos"])
plt.title("Comparación entre concurrencias")
plt.ylabel("Tiempo de concurrencia")
plt.show()
###########################################################################################
###########################################################################################
##########################################################################################
