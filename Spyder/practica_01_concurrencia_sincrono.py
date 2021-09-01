#########################################################################################
##############################################################################################
###############################     A C T I V I D A D    1    ###########################################
#########################################################################################
##############################################################################################
#########################################################################################

import requests
import time 

def descargar_sitio(url, sesion): #Primero se define la función para descargar el sitio
    with sesion.get(url) as respuesta: #Con este comando obtenemos la url del sitio
        print("Leyendo {} de {}".format(len(respuesta.content), url))
            #Nos muestra la longitud del contenido de la url y la url. 

def descargar_todo(sitios): #Esta función va a contener los sitios 
    with requests.Session() as sesion:
        for url in sitios:  #Este cilco descarga la url de los que este contenido en 
            descargar_sitio(url, sesion) #sitios 

if __name__ == '__main__': #Indica al script "el método main" que se ejecutara primero
    sitios =["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
             "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
    #En las líneas de arriba, hacemos una lista con dos sitios web, el cual está 
    #multiplicado por 100
    tiempo_inicio= time.time() #Con la biblioteca time obtenemos el tiempo de inicio
    descargar_todo(sitios) #descargamos todos los sitios contenidos en la lista de arriba
    duracion = time.time()-tiempo_inicio #con esta resta obtenemos el tiempo que se 
                                        #tardo en realizar la descarga
    print('Se descargaron {} sitios en {} segundos'.format(len(sitios), duracion))
  #finalmente este nos muestra cuantos sitios se descargaron y el tiempo que se requirio
#########################################################################################
##############################################################################################
##########################################################################################














