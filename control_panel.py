from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox,
                             QPushButton, QComboBox, QLabel)


class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Группа управления
        control_group = QGroupBox("Управление видео")
        control_layout = QVBoxLayout()

        self.camera_select = QComboBox()
        self.camera_select.addItems(["Тестовое видео", "Камера 1", "Камера 2"])

        self.btn_start = QPushButton("Старт")
        self.btn_stop = QPushButton("Стоп")

        control_layout.addWidget(QLabel("Источник:"))
        control_layout.addWidget(self.camera_select)
        control_layout.addWidget(self.btn_start)
        control_layout.addWidget(self.btn_stop)
        control_group.setLayout(control_layout)

        # Группа действий
        action_group = QGroupBox("Действия")
        action_layout = QVBoxLayout()

        self.btn_snapshot = QPushButton("Снимок")
        self.btn_export = QPushButton("Экспорт данных")

        action_layout.addWidget(self.btn_snapshot)
        action_layout.addWidget(self.btn_export)
        action_group.setLayout(action_layout)

        layout.addWidget(control_group)
        layout.addWidget(action_group)
        layout.addStretch()