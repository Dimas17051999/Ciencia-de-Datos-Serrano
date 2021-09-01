import requests
from bs4 import BeautifulSoup

pagina = requests.get("http://www.arthurleej.com/e-love.html") #obtiene la página de la URL y la guarda 
                                                                #en la variable pagina
print(pagina) #imprime algo
print(pagina.content) #imprime todo  el contenido de la pagina en formato html 

soup = BeautifulSoup(pagina.content, 'html.parser') #función para organizar el contenido de la pagina
print(soup.prettify())                              #en formato html.parser

#<html>
#<head>
#</head>
#<body>
#</body>
#</html>

#cada sección de la página tiene una etiqueta 
titulo = soup.find('b')#esta función busca la etiqueta 'b' y la guarda en la varialbe titulo
print(titulo) #imprime todo lo que hay en titulo, incluyendo texto y etiquetas 
print(titulo.get_text()) #imprimer solamente el texto de la variable 

body = soup.find('body')#esta función busca la etiqueta 'body' y la guarda en la varialbe 
print(body)#imprime todo lo que hay en body, incluyendo texto y etiquetas
print(body.get_text())#imprimer solamente el texto de la variable 

texto_poema = soup.find_all('b') #encuentra todos los elementos 'b', los cuales son 17 para 
                                #este caso, por lo tanto es un elemento iterable 
for texto in texto_poema:  #para cada texto en texto_poema, imprime los elementos que contiene
    print(texto.get_text()) #con esta función imprime solamente el contenido de cada 
                                            #etiqueta
######################################################################################################
pagina = requests.get("http://github.com/Connor-SM") #obtiene el texto de la URL 
soup = BeautifulSoup(pagina.content, 'html.parser' )#le da el formato al contenido en html
                                                    #parser
nombre = soup.find('span', attrs={'class':'vcard-username'}) #esta función encuentra la etiqueta
                #span con el atributo clase llamado vcard-username
print(nombre.get_text()) #imprimer el texto que se guardo en la variable nombre 
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

for seccion in html: 
    print("\n \nNueva Sección")
    print(seccion)

head = list(html.children)[1]

for item in head: 
    print("\n \nNueva Etiqueta")
    print(item)
    
titulo = list(head)[1]
print(titulo.get_text())

######################################################################################################
#Contar el número de palabras del sitio web 
pag = requests.get('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')
soup1 = BeautifulSoup(pag.content, 'html.parser')

import re 
text = soup1.get_text()
number = len(re.findall( r'\w+' , text))
print('El número de palabras son ' + str(number))

















