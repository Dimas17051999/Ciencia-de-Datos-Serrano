##############################################################################################
###############################     A C T I V I D A D    2    ###########################################
#########################################################################################
import time
import requests
import threading #A diferencia de la otra actividad, aqui necesitamos la bilbioteca 
import concurrent.futures # threading y concurrent.futures

# En esta actividad utilizaremos subprocesos para poder hacer más eficientes 
#las descargas , la eficiencia se proporcional al número de núcleos de cada equipo
thread_local= threading.local()

def get_sesion(): #definimos la función para obtener la sesión 
    if not hasattr(thread_local, "session"): #aquí definimos que si no tiene el atributo
        thread_local.session = requests.Session() # sesion, le creamos una sesión 
    return thread_local.session# y aquií le asigna la sesión

def descargar_sitio(url):#Se define la función para descargar el sitio
    sesion = get_sesion() #Con este comando obtenemos la sesión del sitio
    with sesion.get(url) as respuesta:#Con este comando obtenemos la url del sitio
        print("Leyendo {} de {}".format(len(respuesta.content), url))
          #Nos muestra la longitud del contenido de la url y la url.
        
def descargar_todo(sitios): #creamos función para descargar los sitios pero con hilos
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ejecutor: 
    #en la línea de arriba definimos 5 subprocesos queremos para hacer más eficiente
        ejecutor.map(descargar_sitio, sitios) #la descarga y aqui ejecuta la descarga de 
                                              #la url tantas veces como sitios haya 
if __name__ == '__main__': #Indica al script "el método main" que se ejecutara primero
    sitios =["https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html",
           "https://imagenenlaciencia.blogspot.com/2014/08/chamacos-mendigos.html"]*100
   
    #En las líneas de arriba, hacemos una lista con dos sitios web, el cual está 
    #multiplicado por 100    
    tiempo_inicio= time.time()#Con la biblioteca time obtenemos el tiempo de inicio
    descargar_todo(sitios)#descargamos todos los sitios contenidos en la lista de arriba
    duracion_hilos = time.time()-tiempo_inicio#con esta resta obtenemos el tiempo que se 
                                        #tardo en realizar la descarga
    print('Se descargaron {} sitios en {} segundos'.format(len(sitios), duracion_hilos))
























