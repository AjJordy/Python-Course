from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.configStyle()

	def configStyle(self):
		font = self.font()
		font.setPixelSize(MEDIUM_FONT_SIZE)
		# font.setItalic(True)
		# font.setBold(True)
		self.setFont(font)
		self.setMinimumSize(75, 75)
		
		

class ButtonsGrid(QGridLayout):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.configStyle()

		self._gridMask = [
			['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
		]

		self._makeGrid()

	def _makeGrid(self):
		for i, row in enumerate(self._gridMask):
			for j, btnText in enumerate(row):
				button = Button(btnText)
				
				if not isNumOrDot(btnText):
					button.setProperty('cssClass', 'specialButton')

				if btnText == '0':
					self.addWidget(button, i, j, 1, 2)
				elif btnText: 
					self.addWidget(button, i, j)



	def configStyle(self):
		...
