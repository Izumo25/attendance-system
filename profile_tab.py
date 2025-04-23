from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class ProfileTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.name_label = QLabel("Имя: Гость")
        self.email_label = QLabel("Email: не указан")

        # Кнопка для примера
        self.edit_btn = QPushButton("Редактировать профиль")

        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.edit_btn)
        self.setLayout(layout)