'''
Created on Aug 31, 2012

@author: jason
'''
import unittest
import model
from model import TaskView


class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        model.connect_string = 'sqlite:///:memory:' 
        model.echo = True
        model.init()
        model.Task('task1', 'category1')
        model.Task('task2', 'category2')
        model.commit()
       
        
    def setUp(self):
        self.view = model.TaskView()


    def tearDown(self):
        pass


    def testGetNameColumn(self):
        self.assertEqual('name', self.view.columns[TaskView.NAME].id)
        self.assertEqual('Name', self.view.columns[TaskView.NAME].verbose_name)
        self.assertEqual('The name of the task.', self.view.columns[TaskView.NAME].comment)


    def testGetCategoryColumn(self):
        self.assertEqual('category', self.view.columns[TaskView.CATEGORY].id)
        self.assertEqual('Category', self.view.columns[TaskView.CATEGORY].verbose_name)
        self.assertEqual('The category of the task.', self.view.columns[TaskView.CATEGORY].comment)
        

    def testGetMondayTimeColumn(self):
        self.assertEqual('mondayTime', self.view.columns[TaskView.MONDAY_TIME].id)
        self.assertEqual('Monday', self.view.columns[TaskView.MONDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Monday.', self.view.columns[TaskView.MONDAY_TIME].comment)
        

    def testGetTuesdayTimeColumn(self):
        self.assertEqual('tuesdayTime', self.view.columns[TaskView.TUESDAY_TIME].id)
        self.assertEqual('Tuesday', self.view.columns[TaskView.TUESDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Tuesday.', self.view.columns[TaskView.TUESDAY_TIME].comment)
        

    def testGetWednesdayTimeColumn(self):
        self.assertEqual('wednesdayTime', self.view.columns[TaskView.WEDNESDAY_TIME].id)
        self.assertEqual('Wednesday', self.view.columns[TaskView.WEDNESDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Wednesday.', self.view.columns[TaskView.WEDNESDAY_TIME].comment)
        

    def testGetThursdayTimeColumn(self):
        self.assertEqual('thursdayTime', self.view.columns[TaskView.THURSDAY_TIME].id)
        self.assertEqual('Thursday', self.view.columns[TaskView.THURSDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Thursday.', self.view.columns[TaskView.THURSDAY_TIME].comment)
        

    def testGetFridayTimeColumn(self):
        self.assertEqual('fridayTime', self.view.columns[TaskView.FRIDAY_TIME].id)
        self.assertEqual('Friday', self.view.columns[TaskView.FRIDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Friday.', self.view.columns[TaskView.FRIDAY_TIME].comment)
        

    def testGetSaturdayTimeColumn(self):
        self.assertEqual('saturdayTime', self.view.columns[TaskView.SATURDAY_TIME].id)
        self.assertEqual('Saturday', self.view.columns[TaskView.SATURDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Saturday.', self.view.columns[TaskView.SATURDAY_TIME].comment)
        

    def testGetSundayTimeColumn(self):
        self.assertEqual('sundayTime', self.view.columns[TaskView.SUNDAY_TIME].id)
        self.assertEqual('Sunday', self.view.columns[TaskView.SUNDAY_TIME].verbose_name)
        self.assertEqual('The time spent on this task on Sunday.', self.view.columns[TaskView.SUNDAY_TIME].comment)
        
        
    def testGetData(self):
        tasks = self.view.getItems()
        self.assertEqual(2, len(tasks))
        self.assertEqual('task1', tasks[0].name)
        self.assertEqual('category1', tasks[0].category)
        self.assertEqual('task2', tasks[1].name)
        self.assertEqual('category2', tasks[1].category)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetName']
    unittest.main()