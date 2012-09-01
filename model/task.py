'''
Created on Mar 13, 2012

@author: jason
'''
from elixir.entity import Entity
from elixir.fields import Field
from sqlalchemy.types import Unicode, Numeric

class Task(Entity):
    name = Field(Unicode(50))
    category = Field(Unicode(50))
    mondayTime = Field(Numeric(4, 2, True))
    tuesdayTime = Field(Numeric(4, 2, True))
    wednesdayTime = Field(Numeric(4, 2, True))
    thursdayTime = Field(Numeric(4, 2, True))
    fridayTime = Field(Numeric(4, 2, True))
    saturdayTime = Field(Numeric(4, 2, True))
    sundayTime = Field(Numeric(4, 2, True))
    
    
    def __init__(self, name, category=''):
        self.name = name
        self.category = category
        self.mondayTime = 0
        self.tuesdayTime = 0
        self.wednesdayTime = 0
        self.thursdayTime = 0
        self.fridayTime = 0
        self.saturdayTime = 0
        self.sundayTime = 0
        