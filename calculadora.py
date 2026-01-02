import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PySide6.QtCore import Qt


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora - PySide6")
        self.setFixedSize(300, 350)
        self._criar_interface()

    def _criar_interface(self):
        layout_principal = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 20px;")
        layout_principal.addWidget(self.display)

        # Botões
        layout_botoes = QGridLayout()
        botoes = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)
        ]

        for botao in botoes:
            texto = botao[0]
            linha = botao[1]
            coluna = botao[2]
            rowspan = botao[3] if len(botao) > 3 else 1
            colspan = botao[4] if len(botao) > 4 else 1

            btn = QPushButton(texto)
            btn.setFixedHeight(50)
            btn.setStyleSheet("font-size: 16px;")
            btn.clicked.connect(self._acao_botao)

            layout_botoes.addWidget(btn, linha, coluna, rowspan, colspan)

        layout_principal.addLayout(layout_botoes)
        self.setLayout(layout_principal)

    def _acao_botao(self):
        botao = self.sender()
        texto = botao.text()

        if texto == 'C':
            self.display.clear()
        elif texto == '=':
            try:
                resultado = eval(self.display.text())
                self.display.setText(str(resultado))
            except Exception:
                self.display.setText("Erro")
        else:
            self.display.setText(self.display.text() + texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())
