import sys     
from PyQt5.QtWidgets import QWidget,QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout

#Get Item
def getitem():
    for currentItem in table.selectedItems():
        print('Row :',str(currentItem.row()),'Column :',str(currentItem.column()),currentItem.text())

app = QApplication(sys.argv)

#Set widget
wg = QWidget()

#Set title
wg.setWindowTitle('Insert somethings')

#Set size
wg.resize(300,200)

#Create layout
layout=QVBoxLayout()

#Set table
table=QTableWidget()
table.setColumnCount(2)
table.setRowCount(2)

#Set Indexs
Ex = QTableWidgetItem("EX")

#Set Column names
table.setHorizontalHeaderItem(0,QTableWidgetItem("da"))
table.setHorizontalHeaderItem(1,QTableWidgetItem("de"))

#Add items
table.setItem(0,0,QTableWidgetItem("A"))
table.setItem(0,1,QTableWidgetItem("B"))
table.setItem(1,0,QTableWidgetItem("C"))
table.setItem(1,1,QTableWidgetItem("D"))

table.doubleClicked.connect(getitem)
layout.addWidget(table)
wg.setLayout(layout)
wg.show()

sys.exit(app.exec_())
