import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

# class Form(QDialog):
#    def __init__(self, parent=None):
#       super(Form, self).__init__(parent)
		
#       layout = QVBoxLayout()
#       self.b1 = QPushButton("Button1")
#       # self.b1.setCheckable(True)
#       # self.b1.toggle()
#       self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
#       #self.b1.clicked.connect(self.btnstate)
#       layout.addWidget(self.b1)
		
   
#       self.b2 = QPushButton()
#       self.b2.setIcon(QIcon(QPixmap("python.gif")))
#       self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
#       layout.addWidget(self.b2)
#       self.setLayout(layout)
#       self.b3 = QPushButton("Disabled")
#       self.b3.setEnabled(False)
#       layout.addWidget(self.b3)
		
#       self.b4 = QPushButton("&Default")
#       self.b4.setDefault(True)
#       self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
#       layout.addWidget(self.b4)
      
#       self.setWindowTitle("Button demo")

#    # def btnstate(self):
#    #    if self.b1.isChecked():
#    #       print("button pressed")
#    #    else:
#    #       print("button released")
			
#    def whichbtn(self,b):
#       print("clicked button is " +str(b.text()))

# def main():
#    app = QApplication(sys.argv)
#    ex = Form()
#    ex.show()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
#    main()


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullscreenwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *





class Ui_FullScreenWindow(object):
    def setupUi(self, FullScreenWindow):
        FullScreenWindow.setObjectName("FullScreenWindow")
        FullScreenWindow.setWindowModality(QtCore.Qt.WindowModal)
        FullScreenWindow.setEnabled(True)
        FullScreenWindow.resize(1202, 940)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FullScreenWindow.sizePolicy().hasHeightForWidth())
        FullScreenWindow.setSizePolicy(sizePolicy)
        FullScreenWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(FullScreenWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 2, 1115, 745))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pic = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_pic.sizePolicy().hasHeightForWidth())
        self.label_pic = QtWebEngineWidgets.QWebEngineView()
        self.label_pic.setSizePolicy(sizePolicy)
        self.label_pic.setAutoFillBackground(True)
        self.label_pic.setObjectName("label_pic")
        self.verticalLayout.addWidget(self.label_pic)
        FullScreenWindow.setCentralWidget(self.label_pic)

        self.retranslateUi(FullScreenWindow)
        QtCore.QMetaObject.connectSlotsByName(FullScreenWindow)

    def retranslateUi(self, FullScreenWindow):
        _translate = QtCore.QCoreApplication.translate
        FullScreenWindow.setWindowTitle(_translate("FullScreenWindow", "Menu"))

def RunAll():
    app = QApplication(sys.argv)
    window =Ui_FullScreenWindow()
   #  window.show()
    app.exec_()


if __name__=='__main__':
    RunAll()