"""
Author: Aishwarya Sharma
"""
import cherrypy

from src.social import app

if __name__ == '__main__':
	# Starting Server
	app.run(server="cherrypy", host="localhost", port=8080, debug=True, reloader=True)
