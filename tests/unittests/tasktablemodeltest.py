'''
Created on Sep 1, 2012

@author: jason
'''
import unittest
import model

from PySide.QtCore import QModelIndex, Qt


class TaskTableModelTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        model.connect_string = 'sqlite:///:memory:' 
        model.echo = True
        model.init()
        model.Task('task1', 'category1')
        model.Task('task2', 'category2')
        model.Task('task3', 'category3')
        model.Task('task4', 'category4')
        model.commit()


    def setUp(self):
        self.view = model.TaskView()
        self.taskModel = model.TaskTableModel(self.view)
        

    def tearDown(self):
        pass


    def testGetColumnCount(self):
        self.assertEqual(9, self.taskModel.columnCount(QModelIndex()))
        
        
    def testGetRowCount(self):
        self.assertEqual(4, self.taskModel.rowCount(QModelIndex()))
        
        
    def testGetHeaderData(self):
        self.assertEqual('Name', self.taskModel.headerData(0, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Category', self.taskModel.headerData(1, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Monday', self.taskModel.headerData(2, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Tuesday', self.taskModel.headerData(3, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Wednesday', self.taskModel.headerData(4, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Thursday', self.taskModel.headerData(5, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Friday', self.taskModel.headerData(6, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Saturday', self.taskModel.headerData(7, Qt.Horizontal, Qt.DisplayRole))
        self.assertEqual('Sunday', self.taskModel.headerData(8, Qt.Horizontal, Qt.DisplayRole))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()