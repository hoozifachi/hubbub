'''
Created on Mar 13, 2012

@author: jason
'''
import config
import model
import unittest

class TaskTest(unittest.TestCase):


    def setUp(self):
        config.connect_string = 'sqlite:///:memory:' 
        config.echo = True
        model.init()
        

    def tearDown(self):
        model.reset()
        

    def testGetDescription(self):
        task = model.Task('task1')
        self.assertEqual('task1', task.description)


    def testGetID(self):
        task = model.Task('task1')
        model.commit()
        self.assertEqual(1, task.id)
        
        
    def testGetIsCompleted(self):
        task = model.Task('task1')
        self.assertEqual(False, task.is_completed)
                
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()