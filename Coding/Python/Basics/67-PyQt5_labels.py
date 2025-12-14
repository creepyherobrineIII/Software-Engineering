import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #Building blocks of GUI with PyQt5
from PyQt5.QtGui import QFont #For fonts
from PyQt5.QtCore import Qt #To align items


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500) 

        label = QLabel("Hello", self)
        label.setFont(QFont("Times New Roman", 30))
        label.setGeometry(0,0, 500, 100)

        #PyQt5 has styles similar to CSS
        label.setStyleSheet("color: green;" #Can use hexadecimal values
                            "background-color: beige;"
                            "font-weight: bold;"
                            "font-style: italic")
        #label.setAlignment(Qt.AlignTop) #Alligns text to the top vertically
        #label.setAlignment(Qt.AlignBottom) #Alligns text to the bottom vertically
        #label.setAlignment(Qt.AlignVCenter) #Alligns text to the center vertically


        #label.setAlignment(Qt.AlignRight) #Alligns text to the right horizontally
        #label.setAlignment(Qt.AlignHCenter) #Alligns text to the center horizontally
        #label.setAlignment(Qt.AlignLeft) #Alligns text to the left horizontally

        #Method to use both alignment positioning
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center & bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center & Center

        #Shortcut for center positioning
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()