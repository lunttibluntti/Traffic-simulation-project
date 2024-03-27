import sys

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class VehicleGenerationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Traffic simulation - Start menu'
        self.left = 1000
        self.top = 1000
        self.width = 400
        self.height = 140
        self.initUI()
        self.how_many = 0

    def get_how_many(self):
        return self.how_many

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        self.textbox.setValidator(QIntValidator())



        # Create a button in the window
        self.button = QPushButton('Generate', self)
        self.button.move(20, 80)

        # connect button to function
        self.button.clicked.connect(self.set_how_many)

    def set_how_many(self):
        self.how_many = self.textbox.text()
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VehicleGenerationWindow()
    sys.exit(app.exec_())
