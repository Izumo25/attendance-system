from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class DataTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО", "Группа", "Посещаемость"])

        # Тестовые данные
        self.table.setRowCount(3)
        for row in range(3):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.table.setItem(row, 1, QTableWidgetItem(f"Студент {row + 1}"))
            self.table.setItem(row, 2, QTableWidgetItem("Группа 101"))
            self.table.setItem(row, 3, QTableWidgetItem("100%"))

        layout.addWidget(self.table)