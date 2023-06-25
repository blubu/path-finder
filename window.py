
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication


# window function
class DialogueWindow:
    # create window
    def __init__(self):
        self.start = ''
        self.finish = ''

        self.app = QApplication([])
        self.window = QMainWindow()

        # first label
        self.label1 = QLabel('Start Point: ', self.window)
        self.textbox1 = QLineEdit(self.window)
        self.textbox2 = QLineEdit(self.window)

        # second label
        self.label2 = QLabel('Finish Point: ', self.window)
        self.textbox3 = QLineEdit(self.window)
        self.textbox4 = QLineEdit(self.window)

        # algorithm
        self.label3 = QLabel('Algorithm: ', self.window)
        self.dropdown = QComboBox(self.window)
        self.label4 = QLabel('*35 x 35 grid', self.window)

        # run button
        self.push = QPushButton('Run', self.window)

        # set widgets
        self.set_widgets()

        # show window
        self.window.show()

        # button event
        self.push.clicked.connect(self.set_endpoints)

        # app loop
        self.app_exit = self.app.exec()

    def set_widgets(self):
        self.window.setGeometry(500, 300, 300, 200)
        self.window.setFixedSize(300, 200)

        self.label1.setGeometry(25, 25, 75, 30)
        self.label1.setStyleSheet("font-weight:bold")
        self.label2.setGeometry(25, 65, 75, 30)
        self.label2.setStyleSheet("font-weight:bold")
        self.label3.setGeometry(25, 105, 75, 30)
        self.label3.setStyleSheet("font-weight:bold")
        self.label4.setGeometry(25, 145, 80, 30)

        self.textbox1.setPlaceholderText("x1")
        self.textbox1.setGeometry(125, 25, 50, 30)
        self.textbox2.setPlaceholderText("y1")
        self.textbox2.setGeometry(200, 25, 50, 30)
        self.textbox3.setPlaceholderText("x2")
        self.textbox3.setGeometry(125, 65, 50, 30)
        self.textbox4.setPlaceholderText("y2")
        self.textbox4.setGeometry(200, 65, 50, 30)

        self.dropdown.setGeometry(125, 105, 125, 30)
        self.dropdown.addItem('Width First Search')
        self.dropdown.addItem('Depth First Search')
        self.dropdown.addItem('A* Algorithm')

        self.push.setGeometry(180, 145, 70, 30)

    def set_endpoints(self):
        self.start = (int(self.textbox1.text()), int(self.textbox2.text()))
        self.finish = (int(self.textbox3.text()), int(self.textbox4.text()))
        self.window.close()

    def get_endpoints(self):
        return self.start, self.finish



    # checkbox1 = QCheckBox('Show Steps', window)
    # checkbox1.setGeometry(45, 145, 100, 30)
    # checkbox1.setStyleSheet("font-weight:bold")




