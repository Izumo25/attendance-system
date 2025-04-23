from PyQt5.QtWidgets import (
    QDialog, QLabel, QLineEdit,
    QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(600, 400)

        # Инициализация UI
        self.init_ui()

        # Подключение стилей
        self.load_styles()

    def init_ui(self):
        """Инициализация элементов интерфейса"""
        # Основные элементы
        self.label = QLabel("Введите логин и пароль:")
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логин")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Войти")

        # Настройка layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 50)

        # Добавление элементов
        layout.addWidget(self.label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        # Подключение сигналов
        self.login_button.clicked.connect(self.accept)

    def load_styles(self):
        """Загрузка стилей из CSS файла"""
        try:
            with open('ui/styles.css', 'r') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            # Стандартные стили если CSS не найден
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
                }
                QPushButton {
                    background-color: #1e90ff;
                    color: white;
                    border-radius: 4px;
                    padding: 10px;
                    min-width: 100px;
                }
            """)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()