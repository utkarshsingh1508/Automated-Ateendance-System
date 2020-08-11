
from PyQt5 import QtCore, QtGui, QtWidgets
from user import Ui_USER
from admin import Ui_Dialog1
class Ui_main(object):
    def openwindow(self,event):
        self.window= QtWidgets.QDialog()
        self.ui=Ui_USER()
        self.ui.setupUi(self.window)
        self.window.show()
        main.hide()
    def openwindowadmin(self,event):
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Dialog1()
        self.ui.setupUi(self.window)
        self.window.show()
        main.hide()
    def setupUi(self, main):
        main.setObjectName("main")
        main.setWindowModality(QtCore.Qt.NonModal)
        main.setEnabled(True)
        main.resize(1188, 631)
        main.setMinimumSize(QtCore.QSize(1188, 631))
        main.setMaximumSize(QtCore.QSize(1188, 631))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:/project/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setWindowOpacity(1.0)
        main.setStyleSheet("background-image: url(:/newPrefix/imageedit_8_7961532127.jpg);")
        main.setSizeGripEnabled(False)
        main.setModal(False)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(170, 490, 171, 41))
        self.label.setStyleSheet("background: transparent;\n"
"font: 75 12pt \"Times New Roman\";\n"
"color:rgb(85, 0, 127);")
        self.label.setObjectName("label")
        self.label.mousePressEvent=self.openwindowadmin
        self.label_2 = QtWidgets.QLabel(main)
        self.label_2.setGeometry(QtCore.QRect(360, 410, 131, 31))
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 127)")
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent = self.openwindow

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "QWIKLY"))
        self.label.setText(_translate("main", "ADMINISTRATOR"))
        self.label_2.setText(_translate("main", "      USER"))
import xx_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
