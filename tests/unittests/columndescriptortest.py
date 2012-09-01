'''
Created on Aug 31, 2012

@author: jsweet
'''
import unittest

import model

class ColumnDescriptorTest(unittest.TestCase):


    def setUp(self):
        self.descriptor = model.ColumnDescriptor('field_one', 
                                                 'Field one',
                                                 'comment')


    def tearDown(self):
        pass


    def testGetID(self):
        self.assertEqual('field_one', self.descriptor.id)
        
        
    def testGetVerboseName(self):
        self.assertEqual('Field one', self.descriptor.verbose_name)
        
        
    def testGetComment(self):
        self.assertEqual('comment', self.descriptor.comment)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()