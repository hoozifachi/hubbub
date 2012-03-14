from elixir import metadata, setup_all, create_all, session, drop_all
from task import Task
import config


def init():
    metadata.bind = config.connect_string
    metadata.bind.echo = config.echo
    setup_all()
    create_all()
    
def reset():
    session.close()
    drop_all()
    
def commit():
    session.commit()
    