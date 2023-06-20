
from PyQt5.QtWidgets import *


# window function
def dialogue_window(run):
    # create window
    app = QApplication([])
    window = QMainWindow()
    window.setGeometry(500, 300, 500, 400)

    # first label
    label1 = QLabel('Start Point: ', window)
    label1.setGeometry(20, 50, 70, 30)
    textbox1 = QLineEdit(window)
    textbox1.setPlaceholderText("x1")
    textbox1.setGeometry(105, 50, 50, 30)
    textbox2 = QLineEdit(window)
    textbox2.setPlaceholderText("y1")
    textbox2.setGeometry(170, 50, 50, 30)

    # second label
    label2 = QLabel('Finish Point: ', window)
    label2.setGeometry(20, 150, 70, 30)
    textbox3 = QLineEdit(window)
    textbox3.setPlaceholderText("x2")
    textbox3.setGeometry(105, 150, 50, 30)
    textbox4 = QLineEdit(window)
    textbox4.setPlaceholderText("y2")
    textbox4.setGeometry(170, 150, 50, 30)

    # run button
    push = QPushButton('Run', window)
    push.setGeometry(230, 200, 40, 30)

    # show window
    window.show()

    # button event
    push.clicked.connect(lambda: run(textbox1.text(),
                                     textbox2.text(),
                                     textbox3.text(),
                                     textbox4.text(), app))

    # app loop
    app.exec()
