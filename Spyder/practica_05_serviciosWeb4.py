import cherrypy 
import random
import string 

cherrypy.config.update({"server.socket_port":8099})

class Formulario(object):
    @cherrypy.expose
    def index(self):
        return """<html> 
    
                        <head></head>
                        
                          <body>
                          
                            <form method="get" action="generar"> 
                            
                                    <input type="text" value="8" name="longitud"/>
                                    <button type="submit"> Generar Texto </button>
                                    
                            </form>
                          
                            </body>
                        
                  </html>"""
    
    
    @cherrypy.expose
    def generar(self, longitud = 8 ):
        return ''.join(random.sample(string.hexdigits, int(longitud)))
    
if __name__ == '__main__':
    cherrypy.quickstart(Formulario())
