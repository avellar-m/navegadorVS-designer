# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boogiepop/Documents/projects/lmp/navegadorVS-designer/helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelloWorld(object):
    def setupUi(self, HelloWorld):
        HelloWorld.setObjectName("HelloWorld")
        HelloWorld.resize(394, 276)
        self.centralwidget = QtWidgets.QWidget(HelloWorld)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.meuLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.meuLabel.setFont(font)
        self.meuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.meuLabel.setObjectName("meuLabel")
        self.verticalLayout.addWidget(self.meuLabel)
        self.meuBotao = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.meuBotao.setFont(font)
        self.meuBotao.setObjectName("meuBotao")
        self.verticalLayout.addWidget(self.meuBotao)
        HelloWorld.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelloWorld)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 31))
        self.menubar.setObjectName("menubar")
        HelloWorld.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelloWorld)
        self.statusbar.setObjectName("statusbar")
        HelloWorld.setStatusBar(self.statusbar)

        self.retranslateUi(HelloWorld)
        QtCore.QMetaObject.connectSlotsByName(HelloWorld)

    def retranslateUi(self, HelloWorld):
        _translate = QtCore.QCoreApplication.translate
        HelloWorld.setWindowTitle(_translate("HelloWorld", "MainWindow"))
        self.meuLabel.setText(_translate("HelloWorld", "Clique no botão"))
        self.meuBotao.setText(_translate("HelloWorld", "Clique aqui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelloWorld = QtWidgets.QMainWindow()
    ui = Ui_HelloWorld()
    ui.setupUi(HelloWorld)
    HelloWorld.show()
    sys.exit(app.exec_())