from PyQt5.QtWidgets import (
    QDialog, QLabel, QLineEdit,
    QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt
from registration_window import RegistrationWindow  # Убедитесь, что файл существует

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(600, 400)
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 50)

        # Основные элементы
        self.label = QLabel("Введите логин и пароль:")
        self.login_input = QLineEdit(placeholderText="Логин")
        self.password_input = QLineEdit(
            placeholderText="Пароль",
            echoMode=QLineEdit.Password
        )
        self.login_button = QPushButton("Войти")

        # Ссылка на регистрацию
        self.register_label = QLabel(
            '<a href="#" style="color: #1e90ff; text-decoration: none">Создать аккаунт</a>'
        )
        self.register_label.setOpenExternalLinks(False)
        self.register_label.linkActivated.connect(self.show_registration)

        # Добавление элементов
        layout.addWidget(self.label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_label)

        self.setLayout(layout)
        self.login_button.clicked.connect(self.accept)

    # Метод должен быть на уровне класса, а не внутри init_ui!
    def show_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.exec_()

    def load_styles(self):
        """Загрузка стилей из CSS файла"""
        try:
            with open('ui/styles.css', 'r') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            self.setStyleSheet("""
                QLabel { font-size: 16px; font-weight: bold; color: #000; }
                QLineEdit { 
                    min-height: 40px; padding: 5px; 
                    font-size: 14px; border: 1px solid #ccc; 
                }
                QPushButton { 
                    background: #1e90ff; color: white; 
                    border-radius: 4px; padding: 10px; 
                    min-width: 100px; 
                }
            """)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()