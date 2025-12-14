#Essentially text boxes
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Times New Roman;")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Times New Roman;")
        self.line_edit.setPlaceholderText("Enter your name")
        
        #Signals
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()

        print(f"Hello {text}")


def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()