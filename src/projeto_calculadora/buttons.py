
from typing import TYPE_CHECKING

if TYPE_CHECKING: # Avoid circular import 
	from info import Info
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
		self.setFont(font)
		self.setMinimumSize(75, 75)
		# self.setCheckable(True)
		# font.setItalic(True)
		# font.setBold(True)
		

class ButtonsGrid(QGridLayout):
	def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.display = display		
		self.info = info
		self._equation = ''

		self._gridMask = [
			['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0',  '', '.', '='],
		]

		self._makeGrid()

	@property
	def equation(self):
		return self._equation

	@equation.setter
	def equation(self, value):
		self._equation = value
		self.info.setText(value)


	def _makeGrid(self):
		for i, row in enumerate(self._gridMask):
			for j, btnText in enumerate(row):
				button = Button(btnText)
				
				if not isNumOrDot(btnText):
					button.setProperty('cssClass', 'specialButton')
					self._configSpecialButton(button)

				if btnText == '0':
					self.addWidget(button, i, j, 1, 2)
				elif btnText: 
					self.addWidget(button, i, j)

				slot = self._makeSlot(
					self._insertBtnTextToDisplay,
					button
				)
				self._connectButtonClicked(button, slot)

	def _connectButtonClicked(self, button: Button, slot):
		button.clicked.connect(slot)

	def _configSpecialButton(self, button: Button):
		text = button.text()
		if text == 'C':
			# slot = self._makeSlot(self._clear, 'Mensagem')
			# self._connectButtonClicked(button, slot)
			# button.clicked.connect(self.display.clear)
			button.clicked.connect(self._clear)

	def _makeSlot(self, func, *args, **kwargs):
		
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
		

	def _clear(self): #, msg):
		# print('Vou fazer outra coisa', msg)
		self.display.clear()

