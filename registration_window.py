from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class RegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setFixedSize(600, 500)
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 50)

        # Основные элементы
        self.label = QLabel("Создание аккаунта")
        self.email_input = QLineEdit(placeholderText="Email")
        self.name_input = QLineEdit(placeholderText="Имя")
        self.password_input = QLineEdit(
            placeholderText="Пароль",
            echoMode=QLineEdit.Password
        )
        self.confirm_password = QLineEdit(
            placeholderText="Повторите пароль",
            echoMode=QLineEdit.Password
        )
        self.register_btn = QPushButton("Зарегистрироваться")

        # Добавление элементов
        layout.addWidget(self.label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def load_styles(self):
        """Загрузка стилей из CSS файла"""
        try:
            with open('ui/styles.css', 'r') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            self.setStyleSheet("""
                QLabel { 
                    font-size: 16px; 
                    font-weight: bold; 
                    color: #000000; 
                }
                QLineEdit { 
                    min-height: 40px; 
                    padding: 5px; 
                    font-size: 14px; 
                    border: 1px solid #000000; 
                }
                QPushButton { 
                    background-color: #1e90ff; 
                    color: white; 
                    border-radius: 4px; 
                    padding: 10px; 
                    min-width: 100px; 
                }
            """)