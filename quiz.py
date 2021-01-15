import sys
sys.path.append("./src")
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt

# Read in classes
import classes as classHelper

class UI(QWidget):
    def setup(self, Controller):
        self.menuButton = QPushButton("Back to main menu")

        # Hold the widgets
        self.menu = QStackedLayout()
        
        # Pages
        self.menuSelection = QWidget()
        self.classesSelection = QWidget()

        # Call pages, this is first page
        self.beginningMenu()
        self.classesMenu()
        # This is second page
        # INSERT 

        self.menu.addWidget(self.menuSelection)
        self.menu.addWidget(self.classesSelection)

    def beginningMenu(self):
        self.menuSelection.resize(550, 400)
        
        mainLayout = QVBoxLayout()
        menuButtonLayout = QHBoxLayout()

        # Main menu title
        mainMenuTitle = QLabel(self.menuSelection)
        mainMenuTitle.setGeometry(QRect(130, -30, 300, 200))
        mainMenuTitle.setAlignment(Qt.AlignCenter)
        mainMenuTitle.setText("Quiz!")
        mainMenuTitle.setStyleSheet("font: 14pt Century Gothic")
        self.menuSelection.setWindowTitle("Quiz!!")

        self.classesSettings = QPushButton('Classes', self)
        menuButtonLayout.addWidget(self.classesSettings)

        
        mainLayout.addLayout(menuButtonLayout) 
        self.menuSelection.setLayout(mainLayout)

    def classesMenu(self):
        self.classesSelection.resize(550, 400)

        classMainLayout = QVBoxLayout()
        classButtonLayout = QHBoxLayout()

        classEditButtonLayout = QHBoxLayout()

        classMenuTitle = QLabel(self.classesSelection)
        classMenuTitle.setAlignment(Qt.AlignCenter)
        classMenuTitle.setText("Classes")
        classMenuTitle.setStyleSheet("font: 14pt Century Gothic")
        classMenuTitle.adjustSize()
        classMenuTitle.move(50, 100)
        self.classesSelection.setWindowTitle("Quiz!!")

        # Edit classes
        classRemoveButton = QPushButton("Remove class")
        classRemoveButton.resize(100, 20)
        classAddButton = QPushButton("Add class")
        classEditButtonLayout.addWidget(classRemoveButton)
        classEditButtonLayout.addWidget(classAddButton)

        # Setting the classes
        classList = QListWidget()
        currentClasses = classHelper.getClasses()
        for i in currentClasses:
            classList.insertItem(0, i)

    
        # Continue buttons, back
        classButtonLayout.addWidget(self.menuButton, alignment=Qt.AlignRight)
        classContinue = QPushButton("Continue", self)
        classButtonLayout.addWidget(classContinue)

        classMainLayout.addLayout(classButtonLayout)
        classButtonLayout.addWidget(classList)
        classMainLayout.addLayout(classEditButtonLayout)
        self.classesSelection.setLayout(classMainLayout)






class Controller(QMainWindow, UI):
    def  __init__(self):
        super().__init__()
        self.setup(self)

        self.menuButton.clicked.connect(self.menuWindow)
        self.classesSettings.clicked.connect(self.classesMenuSelection)

    def menuWindow(self):
        self.menu.setCurrentIndex(0)

    def classesMenuSelection(self):
        self.menu.setCurrentIndex(1)


def window():
    app = QApplication([])
    ex = Controller()
    sys.exit(app.exec_())


window()
