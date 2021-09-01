# -*- coding: utf-8 -*-

import cherrypy 

cherrypy.config.update({"server.socket_port":8099})

class HolaMundo(object):
    @cherrypy.expose
    def index(self):
        return "Servicio web de Luis Daniel"
    
if __name__ == '__main__':
    cherrypy.quickstart(HolaMundo())


# http://localhost:8099/
# http://127.0.0.1:8099/


