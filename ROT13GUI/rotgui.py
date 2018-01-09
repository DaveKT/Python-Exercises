#!//usr/local/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
    QVBoxLayout, QTextEdit)

def rotate(intext):

	rot13 = str.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return str.translate(intext, rot13)

class ROTWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rotateBtn = QPushButton('Rotate', self)
        rotateBtn.clicked.connect(self.buttonClicked)
        self.text = QTextEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(rotateBtn)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        vbox.addWidget(self.text)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.resize(500, 350)
        self.setWindowTitle('ROT13')
        self.show()

    def buttonClicked(self):
        self.text.setText(rotate(self.text.toPlainText()))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    rot = ROTWindow()
    sys.exit(app.exec_())
