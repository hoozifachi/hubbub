# -*- coding: utf-8 -*-
from lettuce import step
import sys
sys.path.append('../..')
from model import *
setup_all()
create_all()

from elixir import session

@step(u'Given that I have a task object with the name "([^"]*)"')
def given_that_i_have_a_task_object_with_the_name_group1(step, group1):
    Task(name=unicode(group1))

@step(u'When I commit the session')
def when_i_commit_the_session(step):
    session.commit()

@step(u'Then I find "([^"]*)" in the database')
def then_i_find_group1_in_the_database(step, group1):
    task = Task.query.first()
    assert task.name == group1, \
        'Got %s' % task.name
