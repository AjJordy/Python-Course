import sys

from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':	
	app = QApplication(sys.argv)
	setupTheme()
	window = MainWindow()
	icon = QIcon(str(WINDOW_ICON_PATH))
	window.setWindowIcon(icon)	
	window.show()
	app.setWindowIcon(icon)
	app.exec()
	