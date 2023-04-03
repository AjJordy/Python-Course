
from display import Display
from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget


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

		self.display = Display()
		self.display.setPlaceholderText('Digite algo')
		self.vLayout.addWidget(self.display)		

		# Ultima coisa a ser feita
		self.adjustSize()
		self.setFixedSize(self.width(), self.height())