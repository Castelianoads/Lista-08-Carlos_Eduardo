import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolTip, QGridLayout, QWidget
from PyQt5.QtCore import QSize
import subprocess

class Janela(QMainWindow): #MainWindow
    def __init__(self):
        super().__init__()        
        self.setup_main_window()
        self.carregarJanela() #initUI

    def setup_main_window(self):
        self.x = 800
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.wid = QWidget(self) #Cria o widget
        self.setCentralWidget(self.wid) #Fica no centro da janela
        self.layout = QGridLayout() #Cria o layout em grid
        self.wid.setLayout(self.layout) #Aplica o layout grid no widget

    def carregarJanela(self): #initUI
        #Criar os componentes (Label, Button, Text, Image)

        #Criar um label
        self.texto = QLabel("Carlos Eduardo Casteliano de Paula - IFTM", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        #Criando um imagem
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'imagens/arara.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'imagens/arara.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Criando botao
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Abrir imagem") 
        self.botao1.clicked.connect(self.botaoAbrir)

        #Botao 2
        self.botao2 = QtWidgets.QPushButton(self)
        self.botao2.setText("Transformação") 
        self.botao2.clicked.connect(self.botaoTransformar)

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.addWidget(self.botao1, 2, 0)
        self.layout.addWidget(self.botao2, 2, 1)

    #OpenFileDialog
    def botaoAbrir(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Abrir arquivo', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='All files (*.*);; Imagens (*.jpg; *.png)',
                                                            initialFilter='Imagens (*.jpg; *.png)')
        print(fileName)
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def botaoTransformar(self):
        self.entrada = self.endereco1
        self.saida = 'imagens/arquivo_novo.jpg'
        self.script = '.\conversor.py'
        self.programa = 'python ' + self.script + ' ' + self.entrada + ' ' + self.saida
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)


aplicacao = QApplication(sys.argv)        
j = Janela() #MainWindow
j.show()
sys.exit(aplicacao.exec_())
       
