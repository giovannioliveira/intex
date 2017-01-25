# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/giovanni/svm/intex/res/conv.ui'
#
# Created: Tue Jan 24 18:29:55 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btIn = QtWidgets.QPushButton(Dialog)
        self.btIn.setObjectName("btIn")
        self.gridLayout.addWidget(self.btIn, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.btOut = QtWidgets.QPushButton(Dialog)
        self.btOut.setObjectName("btOut")
        self.gridLayout.addWidget(self.btOut, 2, 2, 1, 1)
        self.etIn = QtWidgets.QLineEdit(Dialog)
        self.etIn.setObjectName("etIn")
        self.gridLayout.addWidget(self.etIn, 0, 1, 1, 1)
        self.etOut = QtWidgets.QLineEdit(Dialog)
        self.etOut.setObjectName("etOut")
        self.gridLayout.addWidget(self.etOut, 2, 1, 1, 1)
        self.cbHandler = QtWidgets.QCheckBox(Dialog)
        self.cbHandler.setChecked(True)
        self.cbHandler.setObjectName("cbHandler")
        self.gridLayout.addWidget(self.cbHandler, 1, 0, 1, 1)
        self.etHandler = QtWidgets.QLineEdit(Dialog)
        self.etHandler.setEnabled(False)
        self.etHandler.setObjectName("etHandler")
        self.gridLayout.addWidget(self.etHandler, 1, 1, 1, 1)
        self.btHandler = QtWidgets.QPushButton(Dialog)
        self.btHandler.setEnabled(False)
        self.btHandler.setObjectName("btHandler")
        self.gridLayout.addWidget(self.btHandler, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btBox.setOrientation(QtCore.Qt.Horizontal)
        self.btBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btBox.setObjectName("btBox")
        self.verticalLayout.addWidget(self.btBox)

        self.retranslateUi(Dialog)
        self.btBox.accepted.connect(Dialog.accept)
        self.btBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "intex conversion"))
        self.btIn.setText(_translate("Dialog", "Choose"))
        self.label.setText(_translate("Dialog", "Input file (*.pdf)"))
        self.label_2.setText(_translate("Dialog", "Output dir"))
        self.btOut.setText(_translate("Dialog", "Choose"))
        self.cbHandler.setText(_translate("Dialog", "Default handler"))
        self.btHandler.setText(_translate("Dialog", "Choose"))

