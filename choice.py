# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChoiceWindow(object):
    def setupUi(self, ChoiceWindow):
        ChoiceWindow.setObjectName("ChoiceWindow")
        ChoiceWindow.resize(573, 244)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        ChoiceWindow.setFont(font)
        ChoiceWindow.setStyleSheet("background-color: rgb(200, 197, 193);")
        self.centralwidget = QtWidgets.QWidget(ChoiceWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(200, 197, 193);")
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 100, 310, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox.setStyleSheet("\n"
"background-color: rgb(231, 231, 231);")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 170, 180, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setStyleSheet("QPushButton:enabled{\n"
"  border-radius : 5px;\n"
"  background-color: black;\n"
"  color: white;}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #3e8e41;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        ChoiceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoiceWindow)

    def retranslateUi(self, ChoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "    KTN                                        com port"))
        self.label.setText(_translate("ChoiceWindow", "Выберете  com port"))
        self.pushButton.setText(_translate("ChoiceWindow", "Подключиться"))
