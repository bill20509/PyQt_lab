from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import ui 
import subprocess 
class Main(QMainWindow, ui.Ui_MainWindow):
    def deep_link(self):
        url = self.lineEdit.text()
        command = ["adb", "shell", "am", "start", "-d", url]
        subprocess.run(command)
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.deep_link)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())