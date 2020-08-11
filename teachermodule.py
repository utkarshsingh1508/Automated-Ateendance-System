
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def func3(self):
        os.system("py recognize2.py")
    def func4(self):
        os.system("py spreadsheet.py")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 820)
        Dialog.setMaximumSize(QtCore.QSize(647, 520))
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
        self.pushButton.clicked.connect(self.func3)
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
        self.pushButton_2.clicked.connect(self.func4)
       
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WELCOME TO QWIKLY"))
        self.pushButton.setText(_translate("Dialog", "MARK ATTENDANCE"))
        self.pushButton_2.setText(_translate("Dialog", "GENERATE SPREADSHEET"))
        
import ad_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
