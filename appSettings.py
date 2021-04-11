from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import  QVideoWidget



class App_Window(QMainWindow):

    def __init__(self):
        super(App_Window,self).__init__()
        self.setGeometry(200,50,1500,1000)
        self.setWindowTitle("Noraebang")

        # #create media player
        #
        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #
        # videowidget = QVideoWidget()


class Button():

    def __init__(self,app_window,button_name,x_position,y_position,width,height,font_style):
        self.app_window = app_window
        self.button_name = button_name
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.font_style = font_style

    def set(self):
        button = QtWidgets.QPushButton(self.app_window)
        button.setText(self.button_name)
        button.setGeometry(self.x_position,self.y_position,self.width,self.height)
        button.setFont(self.font_style)

        return button

class Font_Style():

    def __init__(self,font_type,font_size):
        self.font_type = font_type
        self.font_size = font_size

    def set(self):
        font = QFont(self.font_type,self.font_size)

        return font
