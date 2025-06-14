from src.db.db_worker import DBWorker
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QLabel, QTextEdit, QLabel, QComboBox, QPushButton, QDoubleSpinBox, QSpinBox, QHBoxLayout, QMessageBox)
from PySide6.QtCore import Qt, Signal


class AddMaterial(QWidget):
    """
        Виджет - создание материала
    """

    submit_success = Signal() # Событие клика - создание материала
    change_material_requested = Signal() # Событие клика

    def __init__(self):
        super().__init__()
        self.db = DBWorker()

        layout = QVBoxLayout(self)
        header_page = QLabel("Создание материала")
        header_page.setStyleSheet("""
            margin-bottom: 20px;
            font-weight: bold;
            font-size: 24px;
            color: black;
        """)
        layout.addWidget(header_page)

        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("""
            color: black;
        """)
        self.input_field_label = QLabel("Название материала")
        self.input_field_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.input_field_label)
        layout.addWidget(self.input_field)

        self.price = QDoubleSpinBox()
        self.price.setRange(0, 100_000)
        self.price.setStyleSheet("""
            color: black;
        """)
        self.price_label = QLabel("Цена товара")
        self.price_label.setStyleSheet(
            """
                color: black;
                font-weight: bold;
            """
        )
        layout.addWidget(self.price_label)
        layout.addWidget(self.price)

        self.input_quantity = QSpinBox()
        self.input_quantity.setStyleSheet("""
            color: black;
        """)
        self.input_quantity.setRange(1, 100_000)
        self.input_quantity_label = QLabel("Количество материала")
        self.input_quantity_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.input_quantity_label)
        layout.addWidget(self.input_quantity)

        self.input_min_quantity = QSpinBox()
        self.input_min_quantity.setRange(1, 100_000)
        self.input_min_quantity.setStyleSheet("""
            color: black;
        """)
        self.input_min_quantity_label = QLabel("Минимальное количество")
        self.input_min_quantity_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.input_min_quantity_label)
        layout.addWidget(self.input_min_quantity)

        self.input_store_quantity = QSpinBox()
        self.input_store_quantity.setRange(1, 100_000)
        self.input_store_quantity.setStyleSheet("""
            color: black;
        """)
        self.input_store_quantity_label = QLabel("Количество на складе")
        self.input_store_quantity_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.input_store_quantity_label)
        layout.addWidget(self.input_store_quantity)

        self.ed_izm = QLineEdit()
        self.ed_izm.setStyleSheet("""
            color: black;
        """)
        self.ed_izm_label = QLabel("Единица измерения")
        self.ed_izm_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.ed_izm_label)
        layout.addWidget(self.ed_izm)

        # Выпадающий список
        self.combo = QComboBox()
        self.all_material_data = self.db.get_all_material_type()
        self.combo.addItems([mt[1] for mt in self.all_material_data])
        self.combo.setStyleSheet("""
            color: black;
        """)
        self.combo_label = QLabel("Категория")
        self.combo_label.setStyleSheet("""
            color: black;
            font-weight: bold;
        """)
        layout.addWidget(self.combo_label)
        layout.addWidget(self.combo)

        # Кнопка отправки
        self.submit_btn = QPushButton("Сохранить")
        self.submit_btn.setStyleSheet("""
            background-color: #405C73;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
            margin-top: 30px;
        """)
        self.submit_btn.setFixedWidth(150)
        self.submit_btn.clicked.connect(self.submit_event)

        layout.addWidget(self.submit_btn)

    def submit_event(self) -> None:
        """
            Создание материала
        """

        try:
            result = self.db.add_material(
                name_material=self.input_field.text(),
                id_type_material=list(filter(lambda x: x[1] == self.combo.currentText(), self.all_material_data))[0][0],
                price=self.price.value(),
                quantity=self.input_quantity.value(),
                quantity_min=self.input_min_quantity.value(),
                quantity_store=self.input_store_quantity.value(),
                ed=self.ed_izm.text(),
            )
            self.submit_success.emit()
            self.change_material_requested.emit()
        except Exception as ex:
            self.show_error()

    def show_error(self) -> None:
        """
            Создание модального окна с ошибкой
        """

        msg = QMessageBox()
        msg.setWindowTitle("Ошибка создания материала")
        msg.setText("Не удалось создать материал")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()