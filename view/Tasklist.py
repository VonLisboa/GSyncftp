# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect

from globals.constants import CSS


class UiTasklist(object):
    def setup(self, Dialog):
        Dialog.setObjectName("TaskList")
        Dialog.setEnabled(True)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(CSS)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 0, 91, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_status = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_status.setFont(font)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayout_2.addWidget(self.lbl_status)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setFixedHeight(460)
        self.listWidget.setFixedWidth(340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        #self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.retranslate(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GSyncftp - Tasklist"))
        self.lbl_status.setText(_translate("TaskList", "O GSyncftp está atualizado"))
        self.label_2.setText(_translate("TaskList", " Enterprise Coorp. LTDA"))
        self.listWidget.setSortingEnabled(False)
        self.listWidget.addItem("Nenhum arquivo na fila")

    def status_sync(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_status.setText(_translate("TaskList", "Enviando os arquivos..."))

    def status_synced(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_status.setText(_translate("TaskList", "O GSyncftp está atualizado"))

    def do_animation(self, Dialog):
        size_screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        pt_x = size_screen.width() - 339
        pt_y = size_screen.height() - 537
        self.anim = QPropertyAnimation(Dialog, b"geometry")
        self.anim.setDuration(250)
        self.anim.setStartValue(QRect(pt_x, size_screen.height(), 339, 537))
        self.anim.setEndValue(QRect(pt_x, pt_y, 339, 537))
        self.anim.start()
        Dialog.setEnabled(True)

    def not_in_animation(self):
        return self.anim and self.anim.state() != 2


