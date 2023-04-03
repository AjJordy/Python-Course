# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QVBoxLayout, QWidget)

app = QApplication(sys.argv) 
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')

# Buttons
button1 = QPushButton('Text button1')
button2 = QPushButton('Text button2')
button3 = QPushButton('Text button3')
button1.setStyleSheet('font-size: 40px;')

# Layout
# layout = QVBoxLayout()
# layout.addWidget(button)
# layout.addWidget(button2)
layout = QGridLayout()
layout.addWidget(button1,  1, 1) 
layout.addWidget(button2, 1, 2) 
layout.addWidget(button3, 2, 1, 1, 2) 

# Status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')


@Slot()
def slot_example(status_bar):
	def inner():
		status_bar.showMessage('Primeira ação foi clicada')
	return inner


@Slot()
def outro_slot(checked):
	print('checked?', checked)


@Slot()
def terceiro_slot(action):
	def inner():
		outro_slot(action.isChecked())
	return inner


# Menu Bar 
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
segunda_acao = primeiro_menu.addAction('Ação status bar')
segunda_acao.triggered.connect(slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Ação Checkable')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

button1.clicked.connect(terceiro_slot(segunda_acao))

central_widget.setLayout(layout)
# central_widget.show()

window.show()
app.exec()
