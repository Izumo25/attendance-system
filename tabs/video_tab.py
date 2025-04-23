import os
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                            QPushButton, QSlider, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2

class VideoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.cap = None
        self.timer = QTimer()
        self.init_ui()
        self.init_video()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Виджет для видео
        self.video_label = QLabel("Видео не загружено")
        self.video_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.video_label)

        # Панель управления
        control_layout = QHBoxLayout()

        # Кнопка воспроизведения
        self.play_btn = QPushButton("▶")
        self.play_btn.setFixedWidth(40)

        # Слайдер для перемотки
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)

        # Метка времени
        self.time_label = QLabel("00:00 / 00:00")

        control_layout.addWidget(self.play_btn)
        control_layout.addWidget(self.slider)
        control_layout.addWidget(self.time_label)
        layout.addLayout(control_layout)

        # Подключение сигналов
        self.play_btn.clicked.connect(self.toggle_play)
        self.slider.sliderMoved.connect(self.seek_video)

    def init_video(self):
        video_path = os.path.join("videos", "test_video.mp4")
        if os.path.exists(video_path):
            self.cap = cv2.VideoCapture(video_path)
            self.slider.setRange(0, int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)

    def update_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Обновление слайдера
                current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                self.slider.setValue(int(current_frame))

                # Конвертация кадра
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
            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def toggle_play(self):
        if self.timer.isActive():
            self.timer.stop()
            self.play_btn.setText("▶")
        else:
            self.timer.start(30)
            self.play_btn.setText("⏸")

    def seek_video(self, position):
        if self.cap:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            current_time = position / self.cap.get(cv2.CAP_PROP_FPS)
            total_time = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) / self.cap.get(cv2.CAP_PROP_FPS)
            self.time_label.setText(
                f"{self.format_time(current_time)} / {self.format_time(total_time)}"
            )

    def format_time(self, seconds):
        return f"{int(seconds // 60):02}:{int(seconds % 60):02}"

    def closeEvent(self, event):
        if self.cap:
            self.cap.release()
        self.timer.stop()
        super().closeEvent(event)