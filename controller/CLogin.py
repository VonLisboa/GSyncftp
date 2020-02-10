from urllib import request, parse

from PyQt5.QtWidgets import QDialog

from view.Login import UiLogin


class Login(QDialog, UiLogin):
    def __init__(self, login_status, retorno=None, parent=None):
        super(Login, self).__init__(parent)
        self.setup(self)
        self.btnLogin.clicked.connect(self.do_login)
        self.btnCancel.clicked.connect(self.close)
        self.login_status = login_status
        self.retorno = retorno

    def do_login(self):
        url_api = "https://sistemas.lifting.com.br/lifting_ocs/Usuario/login"
        data = parse.urlencode({
            "username": self.username.text(),
            "password": self.passw.text()
        }).encode("utf-8")
        try:
            with request.urlopen(url_api, data) as response:
                # response_text = response.read()
                # print(response_text)
                self.login_status.logged_status = True
                self.close()
                if self.retorno:
                    self.retorno()
        except Exception as err:
            print(err)
            self.lbl_err.show()
