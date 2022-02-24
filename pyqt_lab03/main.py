from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import ui 
import subprocess 
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
## response = requests.get("https://8obm9eihqrvggfz4ml1siq-on.drv.tw/Deeplink/ycp.html")
class Main(QMainWindow, ui.Ui_MainWindow):
    def crawl(self):
        response = requests.get("https://8obm9eihqrvggfz4ml1siq-on.drv.tw/Deeplink/ycp.html")
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all("a")
        deep_list = []
        for item in result:
            temp_list = []
            temp_list.append(item.getText())
            temp_list.append(item.get("href"))
            deep_list.append(temp_list)
        print(deep_list)
        return deep_list
    def deep_link(self):
        index = self.comboBox.currentIndex()
        url = self.deep_list[index][1]
        command = ["adb", "shell", "am", "start", "-d", url]
        subprocess.run(command)
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.deep_link)
        self.deep_list = self.crawl()
        for item in self.deep_list:
            self.comboBox.addItem(item[0])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())