from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
	def __init__(self, parent: QWidget | None=None, *args, **kwargs) -> None:
		super().__init__(parent, *args, **kwargs)

		# Configurando o layout
		self.v_layout = QVBoxLayout()
		self.cw = QWidget()
		self.cw.setLayout(self.v_layout)

		self.label1 = QLabel('O meu testo')
		self.label1.setStyleSheet('font-size: 50px;')
		self.v_layout.addWidget(self.label1)

		self.setCentralWidget(self.cw)
		self.setWindowTitle('Calculadora')

		# Ultima coisa a ser feita
		self.adjustSize()
		self.setFixedSize(self.width(), self.height())