'''
Created on Aug 31, 2012

@author: jason
'''
import model

class TaskView(object):
    
    NAME = 0
    CATEGORY = 1
    MONDAY_TIME = 2
    TUESDAY_TIME = 3
    WEDNESDAY_TIME = 4
    THURSDAY_TIME = 5
    FRIDAY_TIME = 6
    SATURDAY_TIME = 7
    SUNDAY_TIME = 8
    
    columns = []
    
    _col = model.ColumnDescriptor('name', 'Name', 'The name of the task.')
    columns.append(_col)

    _col = model.ColumnDescriptor('category', 'Category', 'The category of the task.')
    columns.append(_col)

    _col = model.ColumnDescriptor('mondayTime', 'Monday', 'The time spent on this task on Monday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('tuesdayTime', 'Tuesday', 'The time spent on this task on Tuesday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('wednesdayTime', 'Wednesday', 'The time spent on this task on Wednesday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('thursdayTime', 'Thursday', 'The time spent on this task on Thursday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('fridayTime', 'Friday', 'The time spent on this task on Friday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('saturdayTime', 'Saturday', 'The time spent on this task on Saturday.')
    columns.append(_col)

    _col = model.ColumnDescriptor('sundayTime', 'Sunday', 'The time spent on this task on Sunday.')
    columns.append(_col)


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def getItems(self):
        return model.Task.query.all()