from PySide.QtCore import SIGNAL, SLOT
from PySide.QtGui import (QDialog, QLabel, QLineEdit, QDialogButtonBox, 
                          QVBoxLayout, QHBoxLayout)
from model import *

class TaskDlg(QDialog):
    def __init__(self, parent=None):
        super(TaskDlg, self).__init__(parent)

        hbox = QHBoxLayout()
        
        nameLabel = QLabel("Name")
        self.nameEdit = QLineEdit()
        
        hbox.addWidget(nameLabel)
        hbox.addWidget(self.nameEdit)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                          QDialogButtonBox.Cancel)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.buttonBox)
        
        self.setLayout(vbox)
        
        self.connect(self.buttonBox, SIGNAL('accepted()'),
                     self, SLOT('accept()'))
        self.setWindowTitle('Task')

    def accept(self):
        Task(name=unicode(self.nameEdit.text()))
        session.commit()

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    app = QApplication(sys.argv)
    dlg = TaskDlg()
    dlg.show()
    app.exec_()