import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500) 

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("garp.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True) #Set contents of label to scale of label

        label.setGeometry((self.width() - label.width()) // 2, #// = integer division (for whole numbers) 
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())

def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()