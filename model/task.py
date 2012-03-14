'''
Created on Mar 13, 2012

@author: jason
'''
from elixir.entity import Entity
from elixir.fields import Field
from sqlalchemy.types import String, Boolean

class Task(Entity):
    description = Field(String(50))
    is_completed = Field(Boolean)
    
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed