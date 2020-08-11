
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def func1(self):
        os.system("py dataset_creator2.py")
    def func2(self):
        os.system("py training.py")
    def func3(self):
        os.system("py recognize2.py")
    def func4(self):
        os.system("py spreadsheetadmin.py")
    def func5(self):
        os.system("py plot.py")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 820)
        Dialog.setMaximumSize(QtCore.QSize(647, 820))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/imageedit_7_7248736798 .jpg);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 200, 641, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"color:rgb(0, 0, 255);\n"
"background: transparent")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.func1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 310, 641, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"color:rgb(0, 0, 255);\n"
"background: transparent")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.func2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 420, 641, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"color:rgb(0, 0, 255);\n"
"background: transparent")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.func3)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 530, 641, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"color:rgb(0, 0, 255);\n"
"background: transparent")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.func4)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 640, 641, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"color:rgb(0, 0, 255);\n"
"background: transparent")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.func5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WELCOME TO QWIKLY"))
        self.pushButton.setText(_translate("Dialog", "Add Student Details To Database"))
        self.pushButton_2.setText(_translate("Dialog", "Add Student Details To System"))
        self.pushButton_3.setText(_translate("Dialog", "Recognise a Student"))
        self.pushButton_4.setText(_translate("Dialog", "Generate Spreadsheet"))
        self.pushButton_6.setText(_translate("Dialog", "Show Database"))
import ad_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
