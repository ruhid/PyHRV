# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\entry.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(686, 571)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.gridLayout.addWidget(self.pushButtonStart, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditPatientFN = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPatientFN.setFont(font)
        self.lineEditPatientFN.setObjectName("lineEditPatientFN")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPatientFN)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditPatientLN = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPatientLN.setFont(font)
        self.lineEditPatientLN.setObjectName("lineEditPatientLN")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditPatientLN)
        self.lineEditPatientD = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPatientD.setFont(font)
        self.lineEditPatientD.setMaxLength(10)
        self.lineEditPatientD.setObjectName("lineEditPatientD")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditPatientD)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dateEditPatientDOB = QtWidgets.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEditPatientDOB.setFont(font)
        self.dateEditPatientDOB.setObjectName("dateEditPatientDOB")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateEditPatientDOB)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 1, 2, 1, 1)
        self.pushButtonOpen = QtWidgets.QPushButton(Dialog)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.gridLayout.addWidget(self.pushButtonOpen, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonStart.setText(_translate("Dialog", "Start "))
        self.label_5.setText(_translate("Dialog", "First name"))
        self.lineEditPatientFN.setInputMask(_translate("Dialog", "AAAAAAAAAAAAAAA"))
        self.label_3.setText(_translate("Dialog", "Laste Name"))
        self.lineEditPatientLN.setInputMask(_translate("Dialog", "AAAAAAAAAAAAAAAAAA"))
        self.lineEditPatientD.setInputMask(_translate("Dialog", "9999999999"))
        self.label_6.setText(_translate("Dialog", "İD"))
        self.label_4.setText(_translate("Dialog", "Date Of Birth"))
        self.label.setText(_translate("Dialog", "Patient İnformation"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))
        self.pushButtonOpen.setText(_translate("Dialog", "Open Existing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())