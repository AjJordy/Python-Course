
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING: # Avoid circular import 
	from display import Display
	from info import Info
	from main_window import MainWindow

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
			self._connectButtonClicked(button, self._clear)

		if text in '+-/*^':
			self._connectButtonClicked(
				button, 
				self._makeSlot(self._operatorClicked, button)
			)

		if text in '=':
			self._connectButtonClicked(button, self._eq)

		if text in  '◀':
			self._connectButtonClicked(button, self.display.backspace)

	def _makeSlot(self, func, *args, **kwargs):		
		@Slot(bool)
		def realSlot(_): 
			func(*args, **kwargs)
		return realSlot

	def _insertBtnTextToDisplay(self, button): 
		buttonText = button.text()		
		newDisplayValue = self.display.text() + buttonText
		if not isValidNumber(newDisplayValue):			
			return 
		
		self.display.insert(buttonText)
		

	def _clear(self): #, msg):
		# print('Vou fazer outra coisa', msg)
		self._left = None
		self._right = None
		self._op = None
		self.equation = ''
		self.display.clear()

	def _operatorClicked(self, button):
		buttonText = button.text()
		displayText = self.display.text()
		self.display.clear()

		if not isValidNumber(displayText) and self._left is None:
			self._showError('Você não escreveu nada')
			return
		
		if self._left is None:
			self._left = float(displayText)

		self._op = buttonText
		self.equation = f'{self._left} {self._op} ??'

	def _eq(self):
		displayText = self.display.text()
	
		if not isValidNumber(displayText):
			self._showError('Você não digitou o outro numero')
			return 
		
		self._right = float(displayText)
		self.equation = f'{self._left} {self._op} {self._right}'
		result = 'error'

		try:
			if '^' in self.equation and isinstance(self._left, float):
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

	def _showInfo(self, text):
		msgBox = self.window.makeMsgBox()
		msgBox.setText(text)
		msgBox.setIcon(msgBox.Icon.Information)
	
	def _showError(self, text):
		msgBox = self.window.makeMsgBox()
		msgBox.setText(text)
		msgBox.setIcon(msgBox.Icon.Critical)
		# msgBox.setStandardButtons(msgBox.StandardButton.NoToAll)
		# msgBox.button(msgBox.StandardButton.NoToAll).setText('Não para todos')
		msgBox.setStandardButtons(
			# msgBox.StandardButton.Cancel |
			# msgBox.StandardButton.Save |
			msgBox.StandardButton.Ok			
		)
		result = msgBox.exec()
		if result == msgBox.StandardButton.Ok: 
			print('ok')
		# elif result == msgBox.StandardButton.Cancel:
		# 	print('cancel')
		# elif result == msgBox.StandardButton.Save:
		# 	print('save')
