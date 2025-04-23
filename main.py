import sys
from PyQt5.QtWidgets import QApplication, QDialog
from login_window import LoginWindow  # Добавлен импорт LoginWindow
from main_window import MainWindow


class App:
    def __init__(self):
        self.auth()

    def auth(self):
        self.login_window = LoginWindow()  # Раскомментирована инициализация
        if self.login_window.exec_() == QDialog.Accepted:
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            sys.exit()


if __name__ == "__main__":  # Исправлена опечатка (было L__main__)
    app = QApplication(sys.argv)

    try:
        # Убедитесь, что путь правильный:
        with open("ui/styles.css", "r", encoding='utf-8') as f:  # Добавьте encoding
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Файл стилей не найден, используются стандартные стили")

    application = App()
    sys.exit(app.exec_())