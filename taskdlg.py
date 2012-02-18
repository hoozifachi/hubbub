from PyQt4.QtGui import QDialog, QLabel, QLineEdit, QDialogButtonBox
from PyQt4.QtCore import SIGNAL, SLOT
from model import *

class TaskDlg(QDialog):
    def __init__(self, parent=None):
        super(TaskDlg, self).__init__(parent)

        nameLabel = QLabel("Name")
        self.nameEdit = QLineEdit()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                          QDialogButtonBox.Cancel)

        self.connect(self.buttonBox, SIGNAL('accepted()'),
                     self, SLOT('accept()'))
        self.setWindowTitle('Task')

    def accept(self):
        Task(name=unicode(self.nameEdit.text()))
        session.commit()

