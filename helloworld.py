import sys
from ui_helloworld import * # arquivo gerado pelo designer

class HelloWorld(Ui_HelloWorld):
    # Classe que herda a classe de UI, conectando funções nas widgets.
    # O arquivo de UI gerado pelo Qt Designer não deve ser modificado.
    def __init__(self, parent=None):
        self.parent = parent
        self.setupUi(parent)
        
        # Conecta o sinal do botão clicado a uma função
        self.meuBotao.clicked.connect(self.funcaoMeuBotao)
    
    def funcaoMeuBotao(self):
        self.meuLabel.setText("Hello World!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = HelloWorld(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
