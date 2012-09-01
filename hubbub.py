'''
Created on Sep 1, 2012

@author: jason
'''
from PySide.QtGui import QApplication, QWidget, QVBoxLayout, QTableView
from model import TaskTableModel
from model import TaskView

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        
        self.layout = QVBoxLayout(self)
        
        self.grid = QTableView()
        self.grid.setModel(TaskTableModel(TaskView()))
        
        self.layout.addWidget(self.grid)

if __name__ == '__main__':
    import sys
    import model
    
    model.connect_string = 'sqlite:///:memory:'
    model.init()
    
    model.Task('task1', 'category1')
    model.Task('task2', 'category1')
    
    model.commit()
    
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()