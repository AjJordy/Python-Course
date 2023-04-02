
import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton,
                               QVBoxLayout, QWidget)

app = QApplication(sys.argv)

button = QPushButton('Text button')
button2 = QPushButton('Text button2')
button3 = QPushButton('Text button3')

button.setStyleSheet('font-size: 40px;')

# layout = QVBoxLayout()
# layout.addWidget(button)
# layout.addWidget(button2)

layout = QGridLayout()
layout.addWidget(button,  1, 1) 
layout.addWidget(button2, 1, 2) 
layout.addWidget(button3, 2, 1, 1, 2) 

widget = QWidget()
widget.setLayout(layout)
widget.show()

app.exec()
