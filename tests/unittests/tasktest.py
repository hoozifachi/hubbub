'''
Created on Mar 13, 2012

@author: jason
'''
import model
import unittest

class TaskTest(unittest.TestCase):


    def setUp(self):
        model.connect_string = 'sqlite:///:memory:' 
        model.echo = True
        model.init()
        

    def tearDown(self):
        model.reset()
        

    def testGetName(self):
        task = model.Task('task1')
        self.assertEqual('task1', task.name)
        
        
    def testGetCategory(self):
        task = model.Task('task1', 'category1')
        self.assertEqual('category1', task.category)
        
        
    def testGetDay0Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.mondayTime)
        

    def testGetDay1Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.tuesdayTime)


    def testGetDay2Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.wednesdayTime)


    def testGetDay3Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.thursdayTime)


    def testGetDay4Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.fridayTime)


    def testGetDay5Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.saturdayTime)


    def testGetDay6Time(self):
        task = model.Task('task1')
        self.assertEqual(0, task.sundayTime)


    def testGetID(self):
        task = model.Task('task1')
        model.commit()
        self.assertEqual(1, task.id)
        
        
    def testTaskIsSaved(self):
        model.Task('task1', True)
        model.commit()
        retTask = model.Task.query.first()
        self.assertEqual('task1', retTask.name)
                
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()