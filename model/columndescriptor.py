'''
Created on Aug 31, 2012

@author: jsweet
'''

class ColumnDescriptor(object):
    '''
    This class defines how columns are depicted in the UI.
    I got this from here - http://stackoverflow.com/a/8360254/1639488.
    '''


    def __init__(self, field_id):
        self.id = field_id
        self.verbose_name = self.id.capitalize().replace('_', ' ')
        self.comment = None
        