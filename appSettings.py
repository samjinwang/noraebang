from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton,QMainWindow,QApplication,QAction,QSlider,QStyle
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import  QVideoWidget



class App_Window(QMainWindow):

    def __init__(self):
        super(App_Window,self).__init__()
        self.setGeometry(200,50,1500,1000)
        self.setWindowTitle("Noraebang")

        # self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #
        # self.video_widget = QVideoWidget(self)
        # self.video_widget.move(100, 100)
        # self.video_widget.setFixedSize(500, 400)
        #
        # self.positionSlider = QSlider(Qt.Horizontal)
        # self.positionSlider.setRange(0, 0)
        # self.positionSlider.sliderMoved.connect(self.set_position)
        #
        # self.play = QPushButton("Play", self)
        # self.play.move(100,500)
        # # self.play.setEnabled(False)
        # self.play.clicked.connect(self.open_file)
        #
        # self.media_player.setVideoOutput(self.video_widget)
        # self.media_player.stateChanged.connect(self.media_state_changed)
        # self.media_player.positionChanged.connect(self.video_position_changed)
        # self.media_player.durationChanged.connect(self.video_duration_changed)
        # self.media_player.error.connect(self.handle_video_error)
        #
        # self.show()
    #
    # def open_file(self):
    #     self.video_file_path = 'love.mp4'
    #     self.video_file_path.play()
    #     # if self.video_file_path != '':
    #     #     self.media_player.setMedia(QMediaContent(
    #     #         QUrl.fromLocalFile(self.video_file_path)))
    #     #     self.update_status_bar(self.video_file_path)
    #     #     self.play()
    #
    # def play(self):
    #     if self.media_player.state() == QMediaPlayer.PlayingState:
    #         self.media_player.pause()
    #         self.pause_play_button.setText("Play")
    #     else:
    #         self.media_player.play()
    #         self.pause_play_button.setText("Pause")
    #
    # def set_position(self, position):
    #     self.mediaPlayer.setPosition(position)
    #
    # def media_state_changed(self, state):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.playButton.setIcon(
    #                 self.style().standardIcon(QStyle.SP_MediaPause))
    #     else:
    #         self.playButton.setIcon(
    #                 self.style().standardIcon(QStyle.SP_MediaPlay))
    #
    # def video_position_changed(self, position):
    #     self.positionSlider.setValue(position)
    #
    # def video_duration_changed(self, duration):
    #     self.positionSlider.setRange(0, duration)
    #
    # def handle_video_error(self):
    #     self.playButton.setEnabled(False)
    #     self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

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
