from elixir import metadata, setup_all, create_all, session, drop_all
from task import Task
from columndescriptor import ColumnDescriptor
from taskview import TaskView
from tasktablemodel import TaskTableModel


connect_string = ''
echo = False


def init():
    metadata.bind = connect_string
    metadata.bind.echo = echo
    setup_all()
    create_all()

    
def reset():
    session.close()
    drop_all()

    
def commit():
    session.commit()
    