

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ui import Ui_MainWindow
import sys
class Main(QMainWindow, Ui_MainWindow):
    def add(self):
        a = self.input_a.toPlainText()
        b = self.input_b.toPlainText()
        sum = int(a) + int(b)
        self.label_3.setText(str(sum))
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calculate.clicked.connect(self.add)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
