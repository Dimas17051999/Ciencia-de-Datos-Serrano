#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:52:28 2021

@author: viridianabadillo
"""
# El mínimo básico en una página HTML:
# <html>
# <head>
# </head>
# <body>
# </body>
# </html>

## Si quiero obtener el cosas...
# todo esto debe hacerse inspeccionando la página, buscando etiquetas
import requests
from bs4 import BeautifulSoup

pagina = requests.get("http://www.arthurleej.com/e-love.html")
print(pagina)

print(pagina.content)

soup = BeautifulSoup(pagina.content,'html.parser')
print(soup.prettify())



## Actividad 1: obtener el título de una página
# Título
pagina = requests.get("http://www.arthurleej.com/e-love.html")
soup = BeautifulSoup(pagina.content,'html.parser')
titulo = soup.find('b') # Encuentra la primera etiqueta b en el HTML
print(titulo.get_text()) # solo texto del título
# Párrafos
texto_poema = soup.find_all('b')
for texto in texto_poema:
    print(texto.get_text())
## Fin Actividad 1

body = soup.find('body') # hay muchísimas cosas
print(body)
print(body.get_text())


## Actividad 2: Connor SM
pagina = requests.get('https://github.com/Connor-SM')
soup = BeautifulSoup(pagina.content,'html.parser')

nombre_usuario = soup.find('span',attrs={'class':'vcard-username'})
print(nombre_usuario.get_text())


## Actividad 3: hijos en soup
pagina = requests.get("http://www.arthurleej.com/e-love.html")
soup = BeautifulSoup(pagina.content,'html.parser')

# Obtener hijo del objeto soup
for child in soup.children:
    print(type(child))
    
# Exploración
html = list(soup.children)[2]

for seccion in html:
    print('\n\nNueva Sección')
    print(seccion)

head = list(html.children)[1]

for item in head:
    print("\n\nNueva Etiqueta")
    print(item)
    
# Mostrar el título del sitio web
titulo = list(head)[1]
print(titulo.get_text())


## Actividad 4: contar el número de palabras de una página
pagina = requests.get("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")
soup = BeautifulSoup(pagina.content,'html.parser')

# Etiqueta que contiene el cuerpo del texto
texto = soup.find_all('body')

# Obtengo únicamente el texto que contenga todo <div> encontrado en una lista
# La lista solo tendrá un elemento
contenido = []
for i in texto:
    contenido.append(i.get_text(' ', strip=True))
#print(contenido) # Despliegue

# Formo lista con una palabra por elemento y quito los '\\'
contenido = ' '.join(contenido).replace('\\','').split()

# Aún quedan los '<', '>' y '-', así que los quitamos
remove = ['<','>','.','-']
for j in range(len(remove)):
    # Esto dejará celdas vacías en la lista
    contenido = [elem.replace(remove[j], '') for elem in contenido]
# Borro celdas vacías de la lista
contenido = list(filter(None, contenido))

# Resultado final: número de palabras en la página
len(contenido)
