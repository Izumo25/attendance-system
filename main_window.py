from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QWidget, QTabWidget,
                             QPushButton, QVBoxLayout, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from control_panel import ControlPanel
from tabs.video_tab import VideoTab
from tabs.data_tab import DataTab
from profile_tab import ProfileTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система видеонаблюдения")
        self.resize(1400, 900)
        self.setMinimumSize(1000, 700)
        self.profile_tab = None
        self.setup_ui()
        self.setup_styles()

    def setup_ui(self):
        # Главный контейнер с вертикальным макетом
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. Верхняя панель с аватаркой
        self.setup_top_bar(main_layout)

        # 2. Основная рабочая область
        work_area = QWidget()
        work_layout = QHBoxLayout(work_area)
        work_layout.setContentsMargins(10, 10, 10, 10)
        work_layout.setSpacing(10)

        # 2.1 Вкладки (70%)
        self.setup_tabs(work_layout)

        # 2.2 Панель управления (30%)
        self.setup_control_panel(work_layout)

        main_layout.addWidget(work_area)

    def setup_top_bar(self, parent_layout):
        top_bar = QWidget()
        top_bar.setFixedHeight(50)
        layout = QHBoxLayout(top_bar)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setAlignment(Qt.AlignRight)

        # Кнопка профиля
        self.profile_btn = QPushButton()
        self.profile_btn.setIcon(QIcon("resources/default_avatar.png"))
        self.profile_btn.setIconSize(QSize(36, 36))
        self.profile_btn.setFlat(True)
        self.profile_btn.setCursor(Qt.PointingHandCursor)
        self.profile_btn.clicked.connect(self.show_profile)

        layout.addWidget(self.profile_btn)
        parent_layout.addWidget(top_bar)

    def setup_tabs(self, parent_layout):
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabPosition(QTabWidget.North)

        self.video_tab = VideoTab()
        self.data_tab = DataTab()

        self.tabs.addTab(self.video_tab, "Видеопоток")
        self.tabs.addTab(self.data_tab, "Данные")

        parent_layout.addWidget(self.tabs, stretch=7)

    def setup_control_panel(self, parent_layout):
        self.control_panel = ControlPanel()
        self.control_panel.setMinimumWidth(350)
        parent_layout.addWidget(self.control_panel, stretch=3)

    def setup_styles(self):
        self.setStyleSheet("""
            /* Основные стили */
            QMainWindow {
                background-color: #ffffff;
            }

            /* Стили вкладок как в первоначальной версии */
            QTabWidget::pane {
                border: 1px solid #d0d0d0;
                margin-top: 5px;
            }

            QTabBar::tab {
                padding: 8px 12px;
                background: #f0f0f0;
                border: 1px solid #d0d0d0;
                margin-right: 2px;
                color: #000000;
            }

            QTabBar::tab:selected {
                background: #ffffff;
                border-bottom: 2px solid #1e90ff;
                color: #1e90ff;
            }

            /* Дополнительные стили */
            QPushButton#profile_btn {
                border: none;
                padding: 2px;
                border-radius: 18px;
            }

            QPushButton#profile_btn:hover {
                background-color: #e0e0e0;
            }
        """)

    def show_profile(self):
        if not self.profile_tab:
            self.profile_tab = ProfileTab()
            self.tabs.addTab(self.profile_tab, "Профиль")
        self.tabs.setCurrentWidget(self.profile_tab)
        self.tabs.setTabVisible(self.tabs.indexOf(self.profile_tab), True)