import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow #Building blocks of GUI with PyQt5
from PyQt5.QtGui import QIcon #For Icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI!")
        #Set position of window on screen using
        self.setGeometry(700, 300, 500, 500) # self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("garp.jpg"))

def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()