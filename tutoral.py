from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def clicked():
  print("clicked")

def window():
  app=QApplication(sys.argv)
  win=QMainWindow()
  win.setGeometry(200,200,300,300)
  win.setWindowTitle("第一下学习")
  label=QtWidgets.QLabel(win)
  label.setText("取号系统")
  label.move(50,50)
  b1=QtWidgets.QPushButton(win)
  b1.setText("Click me")
  b1.clicked.connect(clicked)
  win.show()
  sys.exit(app.exec_())

window()


