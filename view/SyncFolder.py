# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from globals.constants import CSS


class UiSyncFolder(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.resize(273, 115)
        Dialog.setStyleSheet(CSS)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 25, 221, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(120, 60, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.Button_Cancel = QtWidgets.QPushButton(Dialog)
        self.Button_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Cancel.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.Button_Cancel.setObjectName("Button_Cancel")

        self.retranslate(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Manual Synchronize"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Informe a pasta para backup"))
        self.label.setText(_translate("Dialog", ">"))
        self.pushButton.setText(_translate("Dialog", "Enviar"))
        self.Button_Cancel.setText(_translate("Dialog", "Cancelar"))
