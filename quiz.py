from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt
import sys

class UI(QWidget):
    def setup(self, Controller):
        self.menuButton = QPushButton("Back to main menu")

        # Hold the widgets
        self.menu = QStackedLayout()
        
        # Pages
        self.menuSelection = QWidget()

        # Call pages, this is first page
        self.beginningMenu()
        # This is second page
        # INSERT 

        self.menu.addWidget(self.menuSelection)

    def beginningMenu(self):
        self.menuSelection.resize(550, 400)
        
        self.mainLayout = QVBoxLayout()
        self.menuButtonLayout = QHBoxLayout()

        # Main menu title
        self.mainMenuTitle = QLabel(self.menuSelection)
        self.mainMenuTitle.setGeometry(QRect(130, -30, 300, 200))
        self.mainMenuTitle.setAlignment(Qt.AlignCenter)
        self.mainMenuTitle.setText("Quiz!")
        self.mainMenuTitle.setStyleSheet("font: 14pt Century Gothic")
        self.menuSelection.setWindowTitle("Quiz!!")

        self.classesSettings = QPushButton('Classes', self)
        self.menuButtonLayout.addWidget(self.classesSettings)

        
        self.mainLayout.addLayout(self.menuButtonLayout) 
        self.menuSelection.setLayout(self.mainLayout)


class Controller(QMainWindow, UI):
    def  __init__(self):
        super().__init__()
        self.setup(self)

        self.menuButton.clicked.connect(self.menuWindow)

    def menuWindow(self):
        self.menu.setCurrentIndex(0)


def window():
    app = QApplication([])
    ex = Controller()
    sys.exit(app.exec_())


window()
