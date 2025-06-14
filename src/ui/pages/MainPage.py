from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QPixmap
from PySide6 import QtCore

from src.ui.widgets.MainWidget import MainWidget
from src.ui.widgets.AddMaterial import AddMaterial
from src.ui.widgets.ChangeMaterialData import ChangeMaterialData
from src.ui.widgets.Products import ProductWidget


class MainWindow(QMainWindow):
    """
        Основная страница
    """

    change_material_requested = QtCore.Signal(object)

    def __init__(self):
        super().__init__()

        self.change_material_widget = None
        self.setWindowIcon(QIcon("static/icon.ico"))
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            background-color: #FFFFFF;
        """)
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        self.side_panel = QScrollArea()
        self.side_panel.setFixedWidth(200)
        self.side_panel.setWidgetResizable(True)

        self.iconMenu = QLabel()
        self.iconMenu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.iconMenu.setPixmap(QPixmap("static/iconPng.png").scaled(64, 64, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation))
        self.iconMenu.setStyleSheet("""
            QLabel {
                margin-bottom: 100px;
            }
        """)

        self.button_container = QWidget()
        self.button_container.setStyleSheet("""
            QWidget {
                background-color: #BFD6F6;
                border-radius: 5px;
            }
        """)
        self.button_layout = QVBoxLayout(self.button_container)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.button_layout.addWidget(self.iconMenu)

        self.button_main = QPushButton("Главная")
        self.button_create = QPushButton("Создать")

        for btn in [self.button_main, self.button_create]:
            btn.setFixedWidth(150)
            btn.setStyleSheet(
                """
                    QPushButton {
                        background-color: white;
                        color: black;
                        text-align: center;
                        border-radius: 10px;
                        width: 50px;
                    }
                    
                    QPushButton:hover {
                        background-color: #405C73;
                        font-weight: bold;
                        color: white;
                    }
                    
                    QPushButton:checked {
                        background-color: #405C73;
                        color: #FFFFFF;
                    }
                """
            )

        self.buttons = {
            'Главная': self.button_main,
            'Создать': self.button_create,
        }

        for btn in self.buttons.values():
            btn.setCheckable(True)
            btn.clicked.connect(self.switch_page)
            self.button_layout.addWidget(btn)

        self.side_panel.setWidget(self.button_container)

        self.stacked_widget = QStackedWidget()
        self.pages = {
            'Главная': MainWidget(),
            'Создать': AddMaterial(),
        }
        self.pages["Главная"].change_material_requested.connect(self.open_change_material_page)
        self.pages["Создать"].change_material_requested.connect(self.open_add_material)

        for name, widget in self.pages.items():
            self.stacked_widget.addWidget(widget)

        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.stacked_widget)

        self.setStyleSheet("""
            QPushButton {
                padding: 15px;
                border: none;
            }
            QPushButton:checked {
                background-color: black;
            }
        """)

    def switch_page(self):
        """
            Смена содержимого страницы
        """

        btn = self.sender()
        page_name = btn.text().split()[-1]

        if page_name == "Главная":
            self.button_main.setChecked(True)
            self.button_create.setChecked(False)
        else:
            self.button_main.setChecked(False)
            self.button_create.setChecked(True)

        self.stacked_widget.setCurrentWidget(self.pages[page_name])

    def open_change_material_page(self, material_data):
        """
            Переход на страницу изменения данных о материале или на страницу Товаров
        """

        if hasattr(self, "change_material_widget") and self.change_material_widget:
            self.stacked_widget.removeWidget(self.change_material_widget)
            self.change_material_widget.deleteLater()
            self.change_material_widget = None

        if (material_data[-1] == "Product"):
            self.change_material_widget = ProductWidget(material_data)
        else:
            self.change_material_widget = ChangeMaterialData(material_data)
            self.change_material_widget.cancel_clicked.connect(self.back_to_main)
            self.change_material_widget.submit_success.connect(self.back_to_main_and_reload)

        self.stacked_widget.addWidget(self.change_material_widget)
        self.stacked_widget.setCurrentWidget(self.change_material_widget)

    def back_to_main(self, reload: bool = False) -> None:
        """
            Возвращение на главную страницу
        """

        if self.change_material_widget:
            self.stacked_widget.removeWidget(self.change_material_widget)
            self.change_material_widget.deleteLater()
            self.change_material_widget = None

        self.stacked_widget.setCurrentWidget(self.pages["Главная"])

    def back_to_main_and_reload(self) -> None:
        """
            Переход обратно на главную страницу, перерендер содержимого
        """

        if self.change_material_widget:
            self.stacked_widget.removeWidget(self.change_material_widget)
            self.change_material_widget.deleteLater()
            self.change_material_widget = None

        self.stacked_widget.removeWidget(self.pages["Главная"])
        self.pages["Главная"].deleteLater()
        self.pages["Главная"] = MainWidget()

        self.pages['Главная'].change_material_requested.connect(self.open_change_material_page)
        self.stacked_widget.addWidget(self.pages['Главная'])
        self.stacked_widget.setCurrentWidget(self.pages['Главная'])

    def open_add_material(self) -> None:
        """
            Переход на страницу добавления материала
        """

        if self.change_material_widget:
            self.stacked_widget.removeWidget(self.change_material_widget)
            self.change_material_widget.deleteLater()
            self.change_material_widget = None

        self.stacked_widget.removeWidget(self.pages["Главная"])
        self.pages["Главная"].deleteLater()
        self.pages["Главная"] = MainWidget()

        self.pages['Главная'].change_material_requested.connect(self.open_change_material_page)
        self.stacked_widget.addWidget(self.pages['Главная'])
        self.stacked_widget.setCurrentWidget(self.pages['Главная'])