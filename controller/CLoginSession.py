from PyQt5.QtCore import QObject, pyqtSignal


class LoginSession(QObject):
    logged = pyqtSignal(bool)

    def __init__(self):
        QObject.__init__(self)
        self._logged_status = False

    @property
    def logged_status(self):
        return self._logged_status

    @logged_status.setter
    def logged_status(self, val):
        self._logged_status = val
        self.logged.emit(val)
