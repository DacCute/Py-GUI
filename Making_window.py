import sys
from PyQt5.QtWidgets import *

#Set ultility
app = QApplication(sys.argv)

#Create a Widget
w = QWidget()

#Set Title
w.setWindowTitle('This is a window')

#Set window appear direction + size
w.setGeometry(500,500,300,70)

#Resize the window
w.resize(270,50)

#Show Window
w.show()

#Set exit when use close box
sys.exit(app.exec_())