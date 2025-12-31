import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton("Texto do Botão")
botao.setStyleSheet("font-size:40px;")
botao.show()

app.exec()