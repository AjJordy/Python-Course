

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
	def __init__(self, parent=None) -> None:
		super().__init__(parent)

		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)
		self.setWindowTitle('Minha janela')

		# Buttons
		self.button1 = self.make_button('Text button1')
		self.button1.clicked.connect(self.second_action_checked)
		self.button2 = self.make_button('Text button2')
		self.button3 = self.make_button('Text button3')

		# Status Bar
		self.status_bar = self.statusBar()
		self.status_bar.showMessage('Show message on status bar')

		self.grid_layout = QGridLayout()
		self.grid_layout.addWidget(self.button1,  1, 1) 
		self.grid_layout.addWidget(self.button2, 1, 2) 
		self.grid_layout.addWidget(self.button3, 2, 1, 1, 2) 
		self.central_widget.setLayout(self.grid_layout)

		# Menu Bar 
		self.menu = self.menuBar()
		self.primeiro_menu = self.menu.addMenu('First menu')
		self.first_action = self.primeiro_menu.addAction('Action status bar')
		self.first_action.triggered.connect(self.change_status_bar)

		self.second_action = self.primeiro_menu.addAction('Action Checkable')
		self.second_action.setCheckable(True)
		self.second_action.toggled.connect(self.second_action_checked)
		self.second_action.hovered.connect(self.second_action_checked)


	@Slot()
	def change_status_bar(self):		
		self.status_bar.showMessage('First Action triggered')


	@Slot()
	def second_action_checked(self):
		print('checked?', self.second_action.isChecked())
		

	def make_button(self, text):
		btn = QPushButton(text)
		btn.setStyleSheet('font-size: 20px;')
		return btn


	
if __name__ == '__main__':
	app = QApplication(sys.argv) 
	window = MyWindow()
	window.show()
	app.exec()
