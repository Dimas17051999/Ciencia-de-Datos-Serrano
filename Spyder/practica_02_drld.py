import requests
from bs4 import BeautifulSoup
#######################################################################################################
######################                   A C T I V I D A D      1  ###############################
#######################################################################################################
pagina = requests.get("http://www.arthurleej.com/e-love.html") #obtiene la página de la URL y la guarda 
                                                                #en la variable pagina

soup = BeautifulSoup(pagina.content, 'html.parser') #función para organizar el contenido de la pagina

#cada sección de la página tiene una etiqueta 
titulo = soup.find('b')#esta función busca la etiqueta 'b' y la guarda en la varialbe titulo
print(titulo.get_text()) #imprimer solamente el texto de la variable 

texto_poema = soup.find_all('b') #encuentra todos los elementos 'b', los cuales son 17 para 
                                #este caso, por lo tanto es un elemento iterable 
for texto in texto_poema:  #para cada texto en texto_poema, imprime los elementos que contiene
    print(texto.get_text()) #con esta función imprime solamente el contenido de cada 
                                            #etiqueta
                
#######################################################################################################
######################                   A C T I V I D A D         2 #################################
#######################################################################################################
pagina = requests.get("http://github.com/Connor-SM") #obtiene el texto de la URL 
soup = BeautifulSoup(pagina.content, 'html.parser' )#le da el formato al contenido en html
                                                    #parser
nombre = soup.find('span', attrs={'class':'vcard-username'}) #esta función encuentra la etiqueta
                #span con el atributo clase llamado vcard-username
print(nombre.get_text()) #imprimer el texto que se guardo en la variable nombre 

#######################################################################################################
######################                   A C T I V I D A D        3  #################################
#######################################################################################################
pagina = requests.get("http://www.arthurleej.com/e-love.html") #obtiene la página de la URL y la guarda 
                                                                #en la variable pagina
soup = BeautifulSoup(pagina.content, 'html.parser') #función para organizar el contenido de la pagina
                                                                #en formato html.parser
# De la pagina de Arthur Lee 
print(soup.children) #Obtiene cuales son los hijos o dependencias de soup que contiene el contenido 
# debido a que nos dice que es una lista iteratia, los metemos a un ciclo for y además le pedimos que 
#nos muestre el tipo de hijo que es 
for child in soup.children: 
    print(type(child))

html = list(soup.children)[2] # hacemos que soup.children sea una lista y accedemos al elemento 3 

for seccion in html:  #para cada seccion de html, imprimir "Nueva seccion" y a continuación la seccion
    print("\n \nNueva Sección")
    print(seccion)

head = list(html.children)[1] # a través de la variable head accedemos al primer elemento de los hijos de 
                                    # html
for item in head: #para cada item de head, imprimir "Nueva etiqueta" y a continuación cada item
    print("\n \nNueva Etiqueta")
    print(item)
    
titulo = list(head)[1] #accdeemos  al primer elemento de la lista head y lo guardamos en la variable 
print(titulo.get_text()) #titulo para que después se imprima 

#######################################################################################################
######################                   #A C T I V I D A D        4  #################################
####################################################################################################### 
pag = requests.get('https://www.york.ac.uk/teaching/cws/wws/webpage1.html') #Descargo la URL 
soup1 = BeautifulSoup(pag.content, 'html.parser')  #guardo el contenido de la pagina en formato 
                                                    #html parser en la variable soup1
import re #import una libreria para utilizar la función que me permita obtener las palabras 
text = soup1.get_text() #guardo el texto del contenido de soup
print(re.findall( r'\w+' , text)) #Verifico que haya hecho la separación de manera adecuada 
number = len(re.findall( r'\w+' , text)) #con la función re.findall obtengo palabr a por palabra y obtengo
                                                            #su longitud 
print('El número de palabras son ' + str(number)) #imprimo el número de palabras 


















