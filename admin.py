from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from adminwindw import Ui_Dialog

class Ui_Dialog1(object):
    def logincheck(self):
        admin=self.textEdit.toPlainText()
        passwrd=self.textEdit_2.toPlainText()
        connection= sqlite3.connect("login.db")
        result= connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?",(admin,passwrd))
        if(len(result.fetchall())>0):
            self.window=QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.messg("Warning","Invalid Username and Password")
        connection.close()

    def messg(self,title,message):
        mgbox=QtWidgets.QMessageBox()
        mgbox.setIcon(QtWidgets.QMessageBox.Warning)
        mgbox.setWindowTitle(title)
        mgbox.setText(message)
        mgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mgbox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 441)
        Dialog.setMinimumSize(QtCore.QSize(443, 441))
        Dialog.setMaximumSize(QtCore.QSize(443, 441))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/admin.jpg);")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 230, 211, 31))
        self.textEdit.setStyleSheet("background:transparent;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 290, 211, 31))
        self.textEdit_2.setStyleSheet("background:transparent;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 390, 141, 31))
        self.pushButton.setStyleSheet("background:transparent;\n"
"font: 75 14pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.logincheck)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ADMINISTRATOR"))
        self.pushButton.setText(_translate("Dialog", "LOGIN"))
import adm_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
