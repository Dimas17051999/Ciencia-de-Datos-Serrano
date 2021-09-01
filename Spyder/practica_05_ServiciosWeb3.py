import cherrypy 
import random
import string 

cherrypy.config.update({"server.socket_port":8099})

class GenerarTexto(object):
    @cherrypy.expose
    def index(self):
        return "Servicio web de Luis Daniel"
    @cherrypy.expose
    def generar(self, longitud = 8 ):
        return ''.join(random.sample(string.hexdigits, int(longitud)))
    
if __name__ == '__main__':
    cherrypy.quickstart(GenerarTexto())

