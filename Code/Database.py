import sqlite3
from google_trans_new import google_translator
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


class StoredMessage(Base):
    """
    A class for more effectively using the sqlite3 database
    """

    __tablename__ = "messages"

    id_number = Column(Integer, primary_key=True)
    username = Column(String)
    message = Column(String)
    translation = Column(String)

    def __init__(self, id_number, username, message, translation):
        self.id_number = id_number()
        self.username = username()
        self.message = message()
        self.translation = translation()


conn = sqlite3.connect('database.db')

cur = conn.cursor()
