#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
  
import settings
  
DeclarativeBase = declarative_base()
  
def db_connect():
    return create_engine(URL(**settings.DATABASE))
  
def create_dmoz_table(engine):
    DeclarativeBase.metadata.create_all(engine)
  
class Dmoz(DeclarativeBase):
    __tablename__ = "serurity"
    id = Column(Integer, primary_key=True)
    title = Column('title', String(1000))
    link = Column('link', String(1000))
    time = Column('time', String(1000))
    content = Column('content', String(2000))