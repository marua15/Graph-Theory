from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("My Simple GUI")
    window.setGeometry(100, 100, 200, 300)

    layout = QVBoxLayout()

    label = QLabel("Press The Button Below")
    textbox = QTextEdit()
    button = QPushButton("Press Me!")

    button.clicked.connect(lambda : on_clicked(textbox.toPlainText()))
    # clicked is the event
    
    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()

def on_clicked(msg):
    # print("Hello World!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == '__main__' :
    main()