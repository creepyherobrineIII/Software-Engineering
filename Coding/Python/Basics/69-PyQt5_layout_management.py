import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout)

# Need to add a layout manager to a widget because the main window 
# has its own layout, then add the widget to the window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500) 
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color: #fac984;")
        label2.setStyleSheet("background-color: #fab978;")
        label3.setStyleSheet("background-color: #f5a331;")
        label4.setStyleSheet("background-color: #1f7306;")
        label5.setStyleSheet("background-color: #a3fa84;")

        '''
        #VBox Varient
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

        #HBox Varient
        hbox = QHBoxLayout()

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)
        
        '''
        #Grid layout
        grid = QGridLayout()

        grid.addWidget(label1, 0, 0) #(widget, row, column)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)




def main():
    app = QApplication(sys.argv) #Passing this allows PyQt5 to use any commandline arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Allows the app to persist and exit cleanly

if __name__ == "__main__":
    main()