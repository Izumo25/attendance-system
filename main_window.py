from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QTabWidget
from control_panel import ControlPanel
from tabs.video_tab import VideoTab
from tabs.data_tab import DataTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система видеонаблюдения")
        self.resize(1200, 800)
        self.setMinimumSize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        # Главный контейнер
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # 1. Вкладки (левая часть - 70%)
        self.tabs = QTabWidget()
        self.video_tab = VideoTab()
        self.data_tab = DataTab()

        self.tabs.addTab(self.video_tab, "Видеопоток")
        self.tabs.addTab(self.data_tab, "Данные")
        main_layout.addWidget(self.tabs, stretch=7)

        # 2. Панель управления (правая часть - 30%)
        self.control_panel = ControlPanel()
        main_layout.addWidget(self.control_panel, stretch=3)