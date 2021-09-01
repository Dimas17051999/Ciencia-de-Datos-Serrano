# -*- coding: utf-8 -*-
import cherrypy 
import random
import string 

cherrypy.config.update({"server.socket_port":8099})

class GenerarTexto(object):
    @cherrypy.expose
    def index(self):
        return "Servicio web de Luis Daniel"
    @cherrypy.expose
    def generar(self):
        return ''.join(random.sample(string.hexdigits, 8))
    
if __name__ == '__main__':
    cherrypy.quickstart(GenerarTexto())
