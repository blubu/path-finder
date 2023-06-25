
import sys
from PyQt5.QtWidgets import *


# window function
class DialogueWindow:
    # create window
    def __init__(self):
        self.start = ''
        self.finish = ''
        self.algo = ''
        self.label = ''

        self.app = QApplication([])
        self.window = QMainWindow()

        # start label
        self.start_label = QLabel('Start Point: ', self.window)
        self.start_x = QLineEdit(self.window)
        self.start_y = QLineEdit(self.window)

        # final label
        self.finish_label = QLabel('Finish Point: ', self.window)
        self.finish_x = QLineEdit(self.window)
        self.finish_y = QLineEdit(self.window)

        # algorithm dropdown
        self.algo_label = QLabel('Algorithm: ', self.window)
        self.grid_label = QLabel('*35 x 35 grid', self.window)
        self.dropdown = QComboBox(self.window)

        # run button
        self.push = QPushButton('Run', self.window)

        # set widgets
        self.set_widgets()

        # show window
        self.window.show()

        # button event
        self.push.clicked.connect(self.set_endpoints)

        # app loop
        self.app.exec()

    # layout of widgets
    def set_widgets(self):
        self.window.setGeometry(500, 300, 300, 200)
        self.window.setFixedSize(300, 200)

        self.start_label.setGeometry(25, 25, 75, 30)
        self.start_label.setStyleSheet("font-weight:bold")

        self.finish_label.setGeometry(25, 65, 75, 30)
        self.finish_label.setStyleSheet("font-weight:bold")

        self.algo_label.setGeometry(25, 105, 75, 30)
        self.algo_label.setStyleSheet("font-weight:bold")

        self.grid_label.setGeometry(25, 145, 80, 30)

        self.start_x.setPlaceholderText("x1")
        self.start_x.setGeometry(125, 25, 50, 30)

        self.start_y.setPlaceholderText("y1")
        self.start_y.setGeometry(200, 25, 50, 30)

        self.finish_x.setPlaceholderText("x2")
        self.finish_x.setGeometry(125, 65, 50, 30)

        self.finish_y.setPlaceholderText("y2")
        self.finish_y.setGeometry(200, 65, 50, 30)

        self.dropdown.setGeometry(125, 105, 125, 30)
        self.dropdown.addItem('Width First Search')
        self.dropdown.addItem('Depth First Search')
        self.dropdown.addItem('A* Search')

        self.push.setGeometry(180, 145, 70, 30)

    # run function
    def set_endpoints(self):

        self.start = (self.start_x.text(), self.start_y.text())
        self.finish = (self.finish_x.text(), self.finish_y.text())

        if self.start[0] == '' or self.start[1] == '':
            self.start_label.setStyleSheet('color: red;font-weight: bold')
            self.start = (0, 0)
        if self.finish[0] == '' or self.finish[1] == '':
            self.finish_label.setStyleSheet('color: red;font-weight: bold')
            self.finish = (0, 0)

        if self.start != (0, 0) or self.finish != (0, 0):
            self.start = (int(self.start[0]), int(self.start[1]))
            self.finish = (int(self.finish[0]), int(self.finish[1]))

        if self.dropdown.currentIndex() == 0:
            self.algo = 'bfs'
        elif self.dropdown.currentIndex() == 1:
            self.algo = 'dfs'
        else:
            self.algo = 'a*'

        if self.start[0] > 35 or self.start[0] < 1 or self.start[1] > 35 or self.start[1] < 1 or self.finish[0] > 35 \
                or self.finish[0] < 1 or self.finish[1] > 35 or self.finish[1] < 1:
            self.grid_label.setStyleSheet("color: red")
        else:
            self.window.close()

    # function to return the user inputs
    def get_endpoints(self):
        return self.start, self.finish, self.algo


    # checkbox1 = QCheckBox('Show Steps', window)
    # checkbox1.setGeometry(45, 145, 100, 30)
    # checkbox1.setStyleSheet("font-weight:bold")


