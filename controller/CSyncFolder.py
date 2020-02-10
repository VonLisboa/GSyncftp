import os

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QDialog

from view.SyncFolder import UiSyncFolder


class SyncSession(QObject):
    sending_folder = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self._folder = ""

    @property
    def folder_to_send(self):
        return self._folder

    @folder_to_send.setter
    def folder_to_send(self, val):
        self._folder = val
        self.sending_folder.emit(val)


class SyncFolder(QDialog, UiSyncFolder):

    def __init__(self, path, sync_session, parent=None):
        super(SyncFolder, self).__init__(parent)
        QObject.__init__(self)
        self.setup(self)
        self.session = sync_session
        self.path = path
        self.pushButton.clicked.connect(self.__send_folder)
        self.Button_Cancel.clicked.connect(self.close)

    def __send_folder(self):
        if os.path.exists(self.lineEdit.text()):
            self.session.folder_to_send = self.lineEdit.text()
            self.close()
        else:
            # Aviso: folder sem arquivos a serem enviados
            pass
