from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random

from mainUi import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chose_color)

    def chose_color(self):
        old_colors = ["0", "1", "2", "3", "4", "5", "6", "7", "9", "a", "b", "c", "d", "e", "f"]
        new_color = []
        for num in range(6):
            new_color.clear()
            color = random.choices(old_colors, k = 6)
            new_color = color
        
        j = ""
        j = j.join(new_color)
        self.setStyleSheet(f"background: #{j}")
        self.label_2.setText(f"Color: #{j}")

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()