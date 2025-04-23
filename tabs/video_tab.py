import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2


class VideoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_video()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.video_label = QLabel("Видео не загружено")
        self.video_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.video_label)

    def init_video(self):
        video_path = os.path.join("videos", "test_video.mp4")
        if os.path.exists(video_path):
            self.cap = cv2.VideoCapture(video_path)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w

        qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(
            QPixmap.fromImage(qt_image).scaled(
                self.video_label.width(),
                self.video_label.height(),
                Qt.KeepAspectRatio
            )
        )

    def start_video(self):
        if not self.timer.isActive():
            self.timer.start(30)
            self.video_label.setText("")

    def stop_video(self):
        if self.timer.isActive():
            self.timer.stop()
            self.video_label.setText("Видео остановлено")