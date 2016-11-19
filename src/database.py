"""
Author: Aishwarya Sharma
"""

import logging

import sys
from typing import List

from sqlalchemy import and_

from src.Models import User, Post, metadata
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def get_db_session():
	url = "mysql+pymysql://root:root@localhost:3306/social"
	try:
		engine = create_engine(url, echo=True)
		session = sessionmaker(bind=engine)
		new_session = session()
	except:
		logging.warning("Could not connect to database")

	return new_session


def new_user(display_name: str, email: str, password: str) -> bool:
	try:
		session = get_db_session()
		user = User(display_name=display_name, email=email, password=password)
		session.add(user)
		session.commit()
		return True
	except TypeError as err:
		logging.warning("Problem registering new user")
		print(err)
		session.rollback()
	except:
		logging.warning("Problem registering new user")
		session.rollback()
		e = sys.exc_info()[0]
		print("<p>Error: %s</p>" % e)
	return False


def edit_user(): pass


def get_user(): pass


def authenticate_user(email: str, password: str) -> bool:
	try:
		session = get_db_session()
		user = session.query(User).filter(and_(User.email == email, User.password == password)).first()
		if user:
			session.commit()
			return True
	except TypeError as err:
		logging.warning("Problem registering new user")
		logging.error(err)
		session.rollback()
	except:
		logging.warning("Problem registering new user")
		session.rollback()
		e = sys.exc_info()[0]
		logging.error(e)
	return False


def new_post(): pass


def edit_post(): pass


def get_post(id: int=None) -> List[User]:
	posts = []
	try:
		session = get_db_session()
		if id:
			posts = [session.query(Post).filter(Post.id == id).first()]
		else:
			posts = session.query(Post).all()
	except:
		logging.warning("Problem registering new user")
		e = sys.exc_info()[0]
		logging.error(e)

	return posts


def delete_post(id: int): pass
