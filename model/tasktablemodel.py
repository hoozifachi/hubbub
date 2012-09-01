'''
Created on Sep 1, 2012

@author: jason
'''
from PySide import QtCore

class TaskTableModel(QtCore.QAbstractTableModel):

    def __init__(self, view):
        super(TaskTableModel, self).__init__()
        self.view = view
        self.items = view.getItems()
        
        
    def columnCount(self, index):
        return len(self.view.columns)
    
    
    def rowCount(self, index):
        return len(self.items)
    
    
    def headerData(self, column, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.view.columns[column].verbose_name
        
        
    def data(self, index, role):
        if index.isValid():
            if (role == QtCore.Qt.DisplayRole) or (role == QtCore.Qt.EditRole):
                field_name = self.view.columns[index.column()].id
                value = self.items[index.row()].__getattribute__(field_name)
                if value:
                    return unicode(value)
                else:
                    return ''
                
                
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled