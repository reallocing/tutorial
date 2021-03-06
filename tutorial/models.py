#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings
  
DeclarativeBase = declarative_base()

#connect_args={'charset':'utf8'} :解决latin-1的编码问题  
def db_connect():
    return create_engine(URL(**settings.DATABASE),connect_args={'charset':'utf8'},echo = True)
  
def create_dmoz_table(engine):
    DeclarativeBase.metadata.create_all(engine)
  
class Dmoz(DeclarativeBase):
    __tablename__ = "security"
    id = Column(Integer, primary_key=True)
    title = Column('title', String(2000))
    link = Column('link', String(2000))
    time = Column('time', String(2000))
    content = Column('content', String(2000))
  	
