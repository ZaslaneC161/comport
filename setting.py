# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(800, 500)
        Setting.setMinimumSize(QtCore.QSize(800, 500))
        Setting.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Setting)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 90, 70))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.backButton.setObjectName("backButton")
        self.set_modbus = QtWidgets.QPushButton(self.centralwidget)
        self.set_modbus.setEnabled(False)
        self.set_modbus.setGeometry(QtCore.QRect(20, 420, 760, 70))
        self.set_modbus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_modbus.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.set_modbus.setObjectName("set_modbus")
        self.set_name_arrow = QtWidgets.QPushButton(self.centralwidget)
        self.set_name_arrow.setEnabled(False)
        self.set_name_arrow.setGeometry(QtCore.QRect(10, 100, 385, 150))
        self.set_name_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_name_arrow.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.set_name_arrow.setObjectName("set_name_arrow")
        self.set_dtr = QtWidgets.QPushButton(self.centralwidget)
        self.set_dtr.setEnabled(False)
        self.set_dtr.setGeometry(QtCore.QRect(10, 260, 385, 150))
        self.set_dtr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_dtr.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.set_dtr.setObjectName("set_dtr")
        self.hot_hold = QtWidgets.QPushButton(self.centralwidget)
        self.hot_hold.setEnabled(False)
        self.hot_hold.setGeometry(QtCore.QRect(405, 100, 385, 150))
        self.hot_hold.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hot_hold.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.hot_hold.setObjectName("hot_hold")
        self.exit_service = QtWidgets.QPushButton(self.centralwidget)
        self.exit_service.setEnabled(False)
        self.exit_service.setGeometry(QtCore.QRect(405, 260, 385, 150))
        self.exit_service.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_service.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 16pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.exit_service.setObjectName("exit_service")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(520, 20, 260, 70))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 26pt \"Arial Black\";\n"
"border-radius: 15px;\n"
"border-color: rgb(0, 170, 0);\n"
"border-style: solid;\n"
"border-width: 5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 380, 70))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 16pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        Setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "                                                                                 Настроки"))
        self.backButton.setText(_translate("Setting", "<="))
        self.set_modbus.setText(_translate("Setting", "Изменить адрес MODBUS"))
        self.set_name_arrow.setText(_translate("Setting", "Изм. наим. стрелок"))
        self.set_dtr.setText(_translate("Setting", "Привязка ДТ"))
        self.hot_hold.setText(_translate("Setting", "Пороги обогрева"))
        self.exit_service.setText(_translate("Setting", "Вывод из обсл."))
        self.password.setInputMask(_translate("Setting", "***"))
        self.password.setText(_translate("Setting", "***"))
        self.label.setText(_translate("Setting", "Введите PIN код:"))
