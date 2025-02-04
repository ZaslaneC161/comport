# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArrowStat_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArrowStat(object):
    def setupUi(self, ArrowStat):
        ArrowStat.setObjectName("ArrowStat")
        ArrowStat.resize(800, 500)
        ArrowStat.setMinimumSize(QtCore.QSize(800, 500))
        ArrowStat.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(ArrowStat)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 20, 90, 70))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.back.setObjectName("back")
        self.name_arrow = QtWidgets.QLabel(self.centralwidget)
        self.name_arrow.setGeometry(QtCore.QRect(200, 20, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.name_arrow.setFont(font)
        self.name_arrow.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")
        self.name_arrow.setAlignment(QtCore.Qt.AlignCenter)
        self.name_arrow.setObjectName("name_arrow")
        self.t_arrow = QtWidgets.QLabel(self.centralwidget)
        self.t_arrow.setGeometry(QtCore.QRect(610, 45, 180, 75))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.t_arrow.setFont(font)
        self.t_arrow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.t_arrow.setAlignment(QtCore.Qt.AlignCenter)
        self.t_arrow.setObjectName("t_arrow")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 20, 180, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 145, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 145, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 145, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.kalibr = QtWidgets.QPushButton(self.centralwidget)
        self.kalibr.setGeometry(QtCore.QRect(20, 420, 760, 70))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.kalibr.setFont(font)
        self.kalibr.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        self.kalibr.setObjectName("kalibr")
        self.val_ch1 = QtWidgets.QLabel(self.centralwidget)
        self.val_ch1.setGeometry(QtCore.QRect(10, 185, 185, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.val_ch1.setFont(font)
        self.val_ch1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-color: rgb(0, 170, 0);\n"
"border-style: solid;\n"
"border-width: 5px;")
        self.val_ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_ch1.setObjectName("val_ch1")
        self.val_ch2 = QtWidgets.QLabel(self.centralwidget)
        self.val_ch2.setGeometry(QtCore.QRect(10, 295, 185, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.val_ch2.setFont(font)
        self.val_ch2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-color: rgb(0, 170, 0);\n"
"border-style: solid;\n"
"border-width: 5px;")
        self.val_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_ch2.setObjectName("val_ch2")
        self.ch1_info = QtWidgets.QLabel(self.centralwidget)
        self.ch1_info.setGeometry(QtCore.QRect(205, 185, 390, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_info.setFont(font)
        self.ch1_info.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.ch1_info.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_info.setObjectName("ch1_info")
        self.ch2_info = QtWidgets.QLabel(self.centralwidget)
        self.ch2_info.setGeometry(QtCore.QRect(205, 295, 390, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_info.setFont(font)
        self.ch2_info.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.ch2_info.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_info.setObjectName("ch2_info")
        self.ch1_stat = QtWidgets.QLabel(self.centralwidget)
        self.ch1_stat.setGeometry(QtCore.QRect(605, 185, 185, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_stat.setFont(font)
        self.ch1_stat.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.ch1_stat.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_stat.setObjectName("ch1_stat")
        self.ch2_stat = QtWidgets.QLabel(self.centralwidget)
        self.ch2_stat.setGeometry(QtCore.QRect(605, 295, 185, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_stat.setFont(font)
        self.ch2_stat.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.ch2_stat.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_stat.setObjectName("ch2_stat")
        ArrowStat.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArrowStat)
        QtCore.QMetaObject.connectSlotsByName(ArrowStat)

    def retranslateUi(self, ArrowStat):
        _translate = QtCore.QCoreApplication.translate
        ArrowStat.setWindowTitle(_translate("ArrowStat", "MainWindow"))
        self.back.setText(_translate("ArrowStat", "<="))
        self.name_arrow.setText(_translate("ArrowStat", "TextLabel"))
        self.t_arrow.setText(_translate("ArrowStat", "T рельса"))
        self.label_3.setText(_translate("ArrowStat", "Т рельса"))
        self.label_4.setText(_translate("ArrowStat", "Ток"))
        self.label_5.setText(_translate("ArrowStat", "Состояние нагрузки"))
        self.label_6.setText(_translate("ArrowStat", "R изоляции"))
        self.kalibr.setText(_translate("ArrowStat", "Калибровка"))
        self.val_ch1.setText(_translate("ArrowStat", "0"))
        self.val_ch2.setText(_translate("ArrowStat", "0"))
        self.ch1_info.setText(_translate("ArrowStat", "Ток нормальный"))
        self.ch2_info.setText(_translate("ArrowStat", "Ток нормальный"))
        self.ch1_stat.setText(_translate("ArrowStat", "НОРМА"))
        self.ch2_stat.setText(_translate("ArrowStat", "НОРМА"))
