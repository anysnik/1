from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QTextEdit,QApplication, QWidget, QPushButton, QLabel, QVBoxLayout , QHBoxLayout, QRadioButton, QLineEdit,QInputDialog

app = QApplication([])
win = QWidget()

win.resize(700, 400)

win.setWindowTitle("Easy Editor")
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч\Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools)
row.addLayout(col1)
row.addLayout(col2)
win.setLayout(row)

win.show()
app.exec()