
from dz import Ui_MainWindow
from random import *
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication,QMainWindow, QTableWidgetItem

a=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
            '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
            ']', '^', '_', '`', '{', '|', '}', '~']

b = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.height = 2
        self.ui.pushButton_2.clicked.connect(self.degenerat)
        self.ui.horizontalSlider.valueChanged.connect(self.change_slider)



    def degenerat(self):
        self.ui.label_3.setText("Пароль:")
        b = ""
        for i in range(self.height):
            b += choice(a)
        self.ui.label_3.setText(f"Пароль:{b}")


    def change_slider(self, value):
        self.ui.label_2.setText(str(value))
        self.height = value



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
