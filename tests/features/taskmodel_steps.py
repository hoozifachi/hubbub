# -*- coding: utf-8 -*-
from lettuce import step, before, after
import sys
sys.path.append('../..')

import config
import model

@before.each_feature
def setUp(self):
    config.connect_string = 'sqlite:///:memory:' 
    config.echo = True
    model.init()
    
@after.each_feature
def tearDown(self):
    model.reset()
    
@step(u'Given that I have a task object with the name "([^"]*)"')
def given_that_i_have_a_task_object_with_the_name_group1(step, group1):
     model.Task(group1)

@step(u'When I commit the session')
def when_i_commit_the_session(step):
    model.commit()

@step(u'Then I find "([^"]*)" in the database')
def then_i_find_group1_in_the_database(step, group1):
    task = model.Task.query.first()
    assert task.description == group1, \
        'Got %s' % task.description
