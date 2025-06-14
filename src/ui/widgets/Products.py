from src.db.db_worker import DBWorker
from PySide6 import QtCore, QtWidgets


class ProductWidget(QtWidgets.QWidget):
    """
    Виджет списка товаров
    """

    change_material_requested = QtCore.Signal(object) # Сигнал клика кнопки

    def __init__(self, material_data):
        super().__init__()
        self.db = DBWorker()

        self.list_elements = QtWidgets.QScrollArea()
        self.list_elements.setWidgetResizable(True)
        self.container = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setSpacing(10)

        for material in self.db.get_all_products(material_data[0]):
            print(material)
            container = QtWidgets.QWidget()
            container_layout = QtWidgets.QVBoxLayout(container)
            hbox_layout = QtWidgets.QHBoxLayout()
            hbox_layout.addWidget(
                QtWidgets.QLabel(f"{material[-2]} | {material[1]}")
            )
            hbox_layout.addStretch(1)
            hbox_layout.addWidget(QtWidgets.QLabel(f"{material[-1] if material[-1] else '0'}"))
            container_layout.addLayout(hbox_layout)
            container_layout.addWidget(
                QtWidgets.QLabel(f"\nАртикул: {material[2]}\nМинимальная стоимость: {material[-2]}")
            )
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

        label = QtWidgets.QLabel("Список продукции")
        label.setStyleSheet("""
            margin-bottom: 20px;
            color: black;
            font-weight: black;
            font-size: 24px;
        """)

        main_layout.addWidget(label)
        main_layout.addWidget(self.list_elements)
        self.setLayout(main_layout)
