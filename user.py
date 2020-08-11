
from PyQt5 import QtCore, QtGui, QtWidgets
from teacher import Ui_Dialog2
from studentmodule import Ui_Dialog

class Ui_USER(object):
    def openwindowteacher(self,event):
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openwindowstudent(self,event):
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, USER):
        USER.setObjectName("USER")
        USER.resize(296, 448)
        USER.setMinimumSize(QtCore.QSize(296, 448))
        USER.setMaximumSize(QtCore.QSize(296, 448))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        USER.setWindowIcon(icon)
        USER.setStyleSheet("background-image: url(:/newPrefix/page2.jpg);")
        USER.setSizeGripEnabled(False)
        USER.setModal(False)
        self.label = QtWidgets.QLabel(USER)
        self.label.setGeometry(QtCore.QRect(80, 305, 141, 21))
        self.label.setStyleSheet("background:transparent;\n"
"font: 16pt \"Times New Roman\";color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(USER)
        self.label.mousePressEvent=self.openwindowteacher
        self.label_2.setGeometry(QtCore.QRect(80, 370, 141, 31))
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 16pt \"Times New Roman\";color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent=self.openwindowstudent
        self.retranslateUi(USER)
        QtCore.QMetaObject.connectSlotsByName(USER)

    def retranslateUi(self, USER):
        _translate = QtCore.QCoreApplication.translate
        USER.setWindowTitle(_translate("USER", "USER"))
        self.label.setText(_translate("USER", "TEACHER"))
        self.label_2.setText(_translate("USER", "STUDENT"))
import p2_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    USER = QtWidgets.QDialog()
    ui = Ui_USER()
    ui.setupUi(USER)
    USER.show()
    sys.exit(app.exec_())
