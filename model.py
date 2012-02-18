from elixir import *

metadata.bind = 'sqlite:///:memory:'

class Task(Entity):
    name = Field(Unicode(30))

    def __repr__(self):
        return '<Task %s>' % self.name
