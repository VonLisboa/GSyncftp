from PyQt5.QtWidgets import QDialog

from view.Tasklist import UiTasklist


class Tasklist(QDialog, UiTasklist):
    def __init__(self, parent=None):
        super(Tasklist, self).__init__(parent)
        self.setup(self)

    def exec_(self):
        self.do_animation(self)
        super(Tasklist, self).exec_()
