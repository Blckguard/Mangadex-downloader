from PyQt5.QtWidgets import *
from main2 import *

app = QApplication([])
window = QWidget()
URL_input = QTextEdit()
layout = QVBoxLayout()
button = QPushButton('refresh')
chapters = QListWidget()
idkman = QListWidgetItem('let\'s try')

chapters.addItem(idkman)
layout.addWidget(chapters)
layout.addWidget(URL_input)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()

