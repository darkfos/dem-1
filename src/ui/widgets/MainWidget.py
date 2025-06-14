from src.db.db_worker import DBWorker
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    """
        Основной виджет - список материалов
    """

    change_material_requested = QtCore.Signal(object) # Сигнал изменения данных материала

    def __init__(self):
        super().__init__()
        self.db = DBWorker()

        self.list_elements = QtWidgets.QScrollArea()
        self.list_elements.setWidgetResizable(True)
        self.container = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setSpacing(10)

        for material in self.db.get_all_materials():
            container = QtWidgets.QWidget()
            container_layout = QtWidgets.QVBoxLayout(container)
            hbox_layout = QtWidgets.QHBoxLayout()
            hbox_layout.addWidget(
                QtWidgets.QLabel(f"{material[-2]} | {material[1]}")
            )
            hbox_layout.addStretch(1)
            hbox_layout.addWidget(
                QtWidgets.QLabel(f"{material[-1]}")
            )
            container_layout.addLayout(hbox_layout)
            container_layout.addWidget(
                QtWidgets.QLabel(
                                 f"Минимальное количество: {material[5]}\n\n"
                                 f"Количество на складе: {material[4]}\n\n"
                                 f"Цена: {material[3]}р/{material[7]} | {material[6]}")
            )

            hbox_layout = QtWidgets.QHBoxLayout()
            button_material_page = QtWidgets.QPushButton("Изменить")
            button_material_page.setStyleSheet("""
                margin-top: 20px;
                background-color: #405C73;
                color: white;
                font-weight: black;
                padding: 10px;
                border-radius: 5px;
            """)

            button_material_page.setFixedWidth(120)
            button_product_page = QtWidgets.QPushButton("Продукция")
            button_product_page.setStyleSheet("""
                margin-top: 20px;
                background-color: #405C73;
                color: white;
                font-weight: black;
                padding: 10px;
                border-radius: 5px;
            """)
            button_product_page.setFixedWidth(120)
            button_material_page.clicked.connect(lambda checked, m=material: self.change_material_requested.emit((*m, True)))
            button_product_page.clicked.connect(lambda checked, m=material: self.change_material_requested.emit((*m, "Product")))

            hbox_layout.addWidget(button_material_page)
            hbox_layout.addWidget(button_product_page)
            hbox_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

            container_layout.addLayout(hbox_layout)
            container.setLayout(container_layout)
            container.setObjectName("container")
            container.setStyleSheet("""
                #container {
                    color: black;
                    border: 1px solid black;
                    border-radius: 5px;
                }
                
                QLabel {
                    color: black;
                }
            """)
            self.container_layout.addWidget(container)


        self.list_elements.setWidget(self.container)
        main_layout = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel("Главная страница")
        label.setStyleSheet("""
            margin-bottom: 20px;
            color: black;
            font-weight: black;
            font-size: 24px;
        """)

        main_layout.addWidget(label)
        main_layout.addWidget(self.list_elements)
        self.setLayout(main_layout)
