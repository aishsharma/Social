"""
Author: Aishwarya Sharma
"""

import bottle
import logging
import sys
import src.database as db

from bottle import request, redirect
from jinja2 import FileSystemLoader, Environment
from jinja2 import Template

app = bottle.Bottle()
loader = FileSystemLoader("./templates", followlinks=True)
template_env = Environment(loader=loader, optimized=True)


# Return form value in current request
def get_post(value: str):
	return request.forms.get(str(value))


# Returns a jinja2 template for rendering.
def get_template(template_name: str)->Template:
	return template_env.get_template(template_name)


@app.route("/")
def index():
	return get_template("index.html").render()


@app.post("/register")
def do_register():
	try:
		display_name = str(get_post("registerDisplayName"))
		email = str(get_post("registerEmail"))
		password = str(get_post("registerPassword"))
		confirm_password = str(get_post("registerConfirmPassword"))

		if password == confirm_password:
			insert = db.new_user(display_name=display_name, email=email, password=password)
			if insert:
				return "Registered"
			else:
				return "Error registering into system"
		else:
			return get_template("index.html").render(register_err="Passwords did not match")
	except ValueError as err:
		logging.debug(err)
	except TypeError as err:
		logging.debug(err)
	except:
		logging.warning("Unexpected error while registering new member.")
		e = sys.exc_info()[0]
		logging.error(e)


@app.post("/login")
def do_login():
	try:
		email = str(get_post("registerEmail"))
		password = str(get_post("registerPassword"))

		if email and password:
			is_user = db.authenticate_user(email=email, password=password)
			if is_user:
				return "Logged in"
			else:
				return get_template("index.html").render(login_err="Email or password was incorrect")
	except ValueError as err:
		logging.error(err)
	except TypeError as err:
		logging.error(err)
	except:
		logging.warning("Unexpected error while registering logging in.")
		e = sys.exc_info()[0]
		logging.error(e)


@app.get("/feed")
def show_feed():
	pass
