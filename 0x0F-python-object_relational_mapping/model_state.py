#!/usr/bin/python3
'''
Module: creates a state class
'''
import sys
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    '''
    state class representing the state table
    '''
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    name = Column(
        String(128),
        nullable=False
    )
