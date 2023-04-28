
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING: # Avoid circular import 
	from display import Display
	from info import Info
	from main_window import MainWindow

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import convertToNumber, isNumOrDot, isValidNumber
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
	def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.display = display		
		self.info = info
		self.window = window
		self._equation = ''
		self._left = None
		self._right = None
		self._op = None


		self._gridMask = [
			['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
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
		self.display.eqPressed.connect(self._eq)
		self.display.delPressed.connect(self._backspace)
		self.display.clearPressed.connect(self._clear)
		self.display.inputPressed.connect(self._insertToDisplay)
		self.display.operatorPressed.connect(self._configLeftOp)


		for i, row in enumerate(self._gridMask):
			for j, buttonText in enumerate(row):
				button = Button(buttonText)
				
				if not isNumOrDot(buttonText):
					button.setProperty('cssClass', 'specialButton')
					self._configSpecialButton(button)
			 
				self.addWidget(button, i, j)

				slot = self._makeSlot(
					self._insertToDisplay,
					buttonText		
				)
				self._connectButtonClicked(button, slot)

	def _connectButtonClicked(self, button: Button, slot):
		button.clicked.connect(slot)

	def _configSpecialButton(self, button: Button):
		text = button.text()		
		if text == 'C':						
			self._connectButtonClicked(button, self._clear)

		if text in '+-/*^':
			self._connectButtonClicked(
				button, 
				self._makeSlot(self._configLeftOp, text)
			)

		if text == 'N':
			self._connectButtonClicked(button, self._invertNumber)

		if text == '=':
			self._connectButtonClicked(button, self._eq)

		if text ==  '◀':
			self._connectButtonClicked(button, self.display.backspace)


	@Slot()
	def _invertNumber(self):
		displayText = self.display.text()
		if not isValidNumber(displayText):
			return 
		
		number = convertToNumber(displayText) * -1
		self.display.setText(str(number))


	@Slot()
	def _makeSlot(self, func, *args, **kwargs):		
		@Slot(bool)
		def realSlot(_): 
			func(*args, **kwargs)
		return realSlot


	@Slot()
	def _backspace(self):
		self.display.backspace()
		self.display.setFocus()

	@Slot()
	def _insertToDisplay(self, text): 		
		newDisplayValue = self.display.text() + text
		if not isValidNumber(newDisplayValue):			
			return 		
		self.display.insert(text)	
		self.display.setFocus()	
		

	@Slot()
	def _clear(self): 
		self._left = None
		self._right = None
		self._op = None
		self.equation = ''
		self.display.clear()
		self.display.setFocus()


	@Slot()
	def _configLeftOp(self, text):
		displayText = self.display.text()
		self.display.clear()

		if not isValidNumber(displayText) and self._left is None:
			self._showError('Você não escreveu nada')
			return
		
		if self._left is None:
			self._left = convertToNumber(displayText)

		self._op = text
		self.equation = f'{self._left} {self._op} ??'
		self.display.setFocus()
		

	@Slot()
	def _eq(self):
		displayText = self.display.text()
	
		if not isValidNumber(displayText) or self._left is None:
			self._showError('A conta está incompleta')
			return 
		
		self._right = convertToNumber(displayText)
		self.equation = f'{self._left} {self._op} {self._right}'
		result = 'error' 

		try:
			if '^' in self.equation and isinstance(self._left, int | float):
				result = math.pow(self._left, self._right)
			else:
				result = eval(self.equation)
		except ZeroDivisionError:
			self._showError('Divisão por zero')
			print('Zero Division error')
		except OverflowError:
			self._showError('Número muito grande')
			print('Overflow error')
		
		self.display.clear()
		self.info.setText(f'{self.equation} = {result}')
		self._left = result
		self._right = None

		if result == 'error':
			self._left = None

		self.display.setFocus()


	def _showInfo(self, text):
		msgBox = self.window.makeMsgBox()
		msgBox.setText(text)
		msgBox.setIcon(msgBox.Icon.Information)

	
	def _showError(self, text):
		msgBox = self.window.makeMsgBox()
		msgBox.setText(text)
		msgBox.setIcon(msgBox.Icon.Critical)
		msgBox.setStandardButtons(			
			msgBox.StandardButton.Ok			
		)
		result = msgBox.exec()
		if result == msgBox.StandardButton.Ok: 
			print('ok')
		