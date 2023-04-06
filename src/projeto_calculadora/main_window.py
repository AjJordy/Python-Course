
from buttons import Button, ButtonsGrid
from display import Display
from info import Info
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
	def __init__(self, parent: QWidget | None=None, *args, **kwargs) -> None:
		super().__init__(parent, *args, **kwargs)		
		self.setWindowTitle('Calculadora')

		# Configurando o layout
		self.vLayout = QVBoxLayout()
		self.cw = QWidget()
		self.cw.setLayout(self.vLayout)
		self.setCentralWidget(self.cw)

		# self.label1 = QLabel('O meu testo')
		# self.label1.setStyleSheet('font-size: 50px;')
		# self.vLayout.addWidget(self.label1)			

		# Info
		info = Info('')
		self.vLayout.addWidget(info)

		# Display
		self.display = Display()
		# self.display.setPlaceholderText('Digite algo')
		self.vLayout.addWidget(self.display)	

		# Grid
		self.buttonsGrid = ButtonsGrid(self.display, info)
		self.vLayout.addLayout(self.buttonsGrid)		

		# Ultima coisa a ser feita
		self.adjustSize()
		self.setFixedSize(self.width(), self.height())