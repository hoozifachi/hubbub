'''
Created on Aug 31, 2012

@author: jsweet
'''
import unittest

import model

class ColumnDescriptorTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetID(self):
        descriptor = model.ColumnDescriptor('field_one')
        self.assertEqual('field_one', descriptor.id)
        
        
    def testGetVerboseName(self):
        descriptor = model.ColumnDescriptor('field_one')
        self.assertEqual('Field one', descriptor.verbose_name)
        
        
    def testGetComment(self):
        descriptor = model.ColumnDescriptor('field_one')
        descriptor.comment = 'test'
        self.assertEqual('test', descriptor.comment)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()