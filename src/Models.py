# coding: utf-8
import email

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Post(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key=True)
	user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
	content = Column(String, nullable=False)
	create_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
	last_update = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

	user = relationship('User')

	def __init__(self, user_id: int, content: str):
		self.user_id = user_id
		self.content = content


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	display_name = Column(String(100), nullable=False, unique=True)
	email = Column(String(100), nullable=False, unique=True)
	password = Column(String(100), nullable=False)
	join_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

	def __init__(self, display_name: str, email: str, password: str):
		self.display_name = display_name
		self.email = email
		self.password = password
