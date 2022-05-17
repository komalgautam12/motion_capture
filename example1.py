from  motioncapture import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt




class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("C:\\Users\\samsa\\OneDrive\\Documents\\GitHub\\motion_capture\\project1.ui", self)
        # click logic for button
        self.pushButton.clicked.connect(self.clicked)

   
    def clicked(self):

        fname= QFileDialog.getOpenFileName(self,'open file','C:\\Users\\samsa\\OneDrive\\Desktop\\chemistry')
        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
   