
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sqlite3

import numpy as np
import matplotlib.pyplot as plt


class Ui_Dialog(object):
    def findattendance(self):
        rollno=self.textEdit.toPlainText()
        connection= sqlite3.connect('Face-DataBase3')
        result= connection.execute("SELECT Name,Presents FROM Students WHERE Roll= ?",(rollno,))
        x=result.fetchall()
        if(len(x)>0):
            Name = []
            Presents = []
            data=x
            
            for row in data:
                Name.append(row[0])
                Presents.append(row[1])
            plt.figure()

            n_groups = len(Presents)

            index = np.arange(n_groups)

            plt.bar(index,Presents,align='center')


            plt.xlabel('Name')
            plt.ylabel('Presents')
            plt.title('Attendance of Student')
            plt.xticks(index,Name)
            plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', 
            labelbottom='on')
            plt.show()
            self.connection.close()
        else:
            self.messg("Warning","Invalid Roll Number")

    def messg(self,title,message):
        mgbox=QtWidgets.QMessageBox()
        mgbox.setIcon(QtWidgets.QMessageBox.Warning)
        mgbox.setWindowTitle(title)
        mgbox.setText(message)
        mgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mgbox.exec_()
        
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
        self.pushButton.setGeometry(QtCore.QRect(0, 420, 641, 91))
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
        self.pushButton.clicked.connect(self.findattendance)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(4, 310, 641, 91))
        self.textEdit.setStyleSheet("background:transparent;")
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 200, 641, 91))
        self.label.setStyleSheet("background: transparent;\n"
"font: 95 20pt \"Times New Roman\";\n"
"color:rgb(85, 0, 127);")
        self.label.setObjectName("label")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WELCOME TO QWIKLY"))
        self.label.setText(_translate("Dialog", "ENTER THE ROLLNO"))
        self.pushButton.setText(_translate("Dialog", "FIND"))

        
import ad_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
