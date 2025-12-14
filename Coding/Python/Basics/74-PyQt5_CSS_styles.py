import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1") #Using a layout manager allows you to not add "self" param
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        #Necessary to set styling individually
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Times New Roman;
                padding: 15px 75px;
                margin: 25px;     
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: #fac984;
            }
            QPushButton#button2{
                background-color: #f59f49;
            }
            QPushButton#button3{
                background-color: #f5a331;    
            }
            QPushButton#button1:hover{
                background-color: #f5d9b3;
            }
            QPushButton#button2:hover{
                background-color: #fab978;
            }
            QPushButton#button3:hover{
                background-color: #ad7f3e;
            }
        """)


def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()