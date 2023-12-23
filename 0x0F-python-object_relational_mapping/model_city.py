#!/usr/bin/python3
'''
Module: creates a state class
'''
import sys
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


class City(Base):
    '''
    city class representing the city table
    '''
    __tablename__ = 'cities'
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

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )

    state = relationship('State')
