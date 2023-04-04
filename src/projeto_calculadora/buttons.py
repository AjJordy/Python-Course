from display import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isNumOrDot, isValidNumber
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
		# self.setCheckable(True)
		

class ButtonsGrid(QGridLayout):
	def __init__(self, display: Display, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.display = display		

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

				buttonSlot = self._makeBtnDisplaySlot(
					self._insertBtnTextToDisplay,
					button
				)
				button.clicked.connect(buttonSlot)

	def _makeBtnDisplaySlot(self, func, *args, **kwargs):
		@Slot(bool)
		def realSlot(_): 
			func(*args, **kwargs)
		return realSlot

	def _insertBtnTextToDisplay(self, button): # checked
		buttonText = button.text()
		newDisplayValue = self.display.text()
		if not isValidNumber(newDisplayValue):
			return 
		
		self.display.insert(buttonText)
		



