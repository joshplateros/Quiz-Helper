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
        self.menuSelection.resize(750, 500)
        
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
        self.classesSelection.resize(750, 500)

        classMainLayout = QVBoxLayout()
        classButtonLayout = QHBoxLayout()

        classEditButtonLayout = QHBoxLayout()

        classMenuTitle = QLabel(self.classesSelection)
        classMenuTitle.setAlignment(Qt.AlignCenter)
        classMenuTitle.setText("Classes")
        classMenuTitle.setStyleSheet("font: 14pt Century Gothic")
        classMenuTitle.adjustSize()
        classMenuTitle.move(30, 100)
        self.classesSelection.setWindowTitle("Quiz!!")

        # Edit classes
        classRemoveButton = QPushButton("Remove class")
        classRemoveButton.resize(100, 20)
        classAddButton = QPushButton("Add class")
        classEditButtonLayout.addWidget(classRemoveButton)
        classEditButtonLayout.addWidget(classAddButton)

        # Setting the classes
        self.classList = QListWidget()
        self.currentClasses = classHelper.getClasses()
        for i in self.currentClasses:
            self.classList.insertItem(0, i)
        
        classContinue = QPushButton("Continue", self)

        # Grey out continue button
        classContinue.setDisabled(True)
        self.classList.itemSelectionChanged.connect(lambda: classContinue.setDisabled(False))
        
        # Add / Remove classes
        classRemoveButton.clicked.connect(self.removeClass)
        classAddButton.clicked.connect(self.addClass)

        # Return to menu button
        classButtonLayout.addWidget(self.menuButton, alignment=Qt.AlignRight)

        # Continue (save classes and move on)
        classContinue.clicked.connect(lambda: classHelper.saveClasses(self.currentClasses))


        classMainLayout.addLayout(classButtonLayout)
        classButtonLayout.addWidget(self.classList)
        classButtonLayout.addWidget(classContinue)
        classMainLayout.addLayout(classEditButtonLayout)
        self.classesSelection.setLayout(classMainLayout)

    def removeClass(self):
        if not self.classList: return
        for item in self.classList.selectedItems():
            self.classList.takeItem(self.classList.row(item))
        self.currentClasses = []
        # Update classes
        for index in range(0, self.classList.count()):
            self.currentClasses.append(self.classList.item(index).text())

    def addClass(self):
        classNameText, classNameConfirm = QInputDialog.getText(self, "User class name: ", "Enter the class to add")
        if classNameConfirm:
            exists = False
            for x in self.currentClasses:
                if x == classNameText:
                    exists = True
            if exists == False:
                self.classList.insertItem(len(self.currentClasses), classNameText)
        self.currentClasses = []
        for index in range(0, self.classList.count()):
            self.currentClasses.append(self.classList.item(index).text())













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
