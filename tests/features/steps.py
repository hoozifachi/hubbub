# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append('../..')
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

import taskdlg
import model
import config

@before.each_feature
def setUp(self):
    config.connect_string = 'sqlite:///:memory:' 
    config.echo = True
    model.init()
    
@after.each_feature
def tearDown(self):
    model.reset()
        
@step(u'Given that I have a task editor')
def given_that_i_have_a_task_editor(step):
    world.app = QApplication(sys.argv)
    world.dlg = taskdlg.TaskDlg()

@step(u'When I enter "([^"]*)" in the task name')
def when_i_enter_group1_in_the_task_name(step, group1):
    world.dlg.nameEdit.setText(group1)

@step(u'And I press the OK button')
def and_i_press_the_ok_button(step):
    okButton = world.dlg.buttonBox.button(world.dlg.buttonBox.Ok)
    QTest.mouseClick(okButton, Qt.LeftButton)

@step(u'Then I see "([^"]*)"')
def then_i_see_group1(step, group1):
    task = model.Task.query.first()
    assert task.description == group1, \
        'Got %s' % task.description

