from src.db.db_worker import DBWorker
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QLabel, QTextEdit, QLabel, QComboBox, QPushButton, QDoubleSpinBox, QSpinBox, QHBoxLayout, QMessageBox)
from PySide6.QtCore import Qt, Signal


class ChangeMaterialData(QWidget):
    """
        Виджет - изменение данных о материале
    """

    cancel_clicked = Signal() # Сигнал клика кнопки - Отмена
    submit_success = Signal() # Сигнал клика кнопки - Изменить

    def __init__(self, material_data):
        super().__init__()
        self.db = DBWorker()
        self.material_data = material_data # Изначальные данные материала

        layout = QVBoxLayout(self)
        header_page = QLabel("Редактирование - {}".format(material_data[1]))
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
        self.input_field.setText(material_data[1])
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
        self.price.setValue(float(material_data[3]))
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
        self.input_quantity.setValue(material_data[4])
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
        self.input_min_quantity.setValue(material_data[5])
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
        self.input_store_quantity.setValue(material_data[6])
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
        self.ed_izm.setText(material_data[7])
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

        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.setStyleSheet("""
            background-color: #405C73;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
            margin-top: 30px;
        """)
        self.cancel_btn.setFixedWidth(150)
        self.cancel_btn.clicked.connect(self.cancel_clicked.emit)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.submit_btn)
        self.button_layout.addWidget(self.cancel_btn)
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(self.button_layout)

    def submit_event(self) -> None:
        """
            Изменение данных материала
        """
        try:
            self.db.update_material_data(
                name_material=self.input_field.text(),
                id_type_material=list(filter(lambda x: x[1] == self.combo.currentText(), self.all_material_data))[0][0],
                price=self.price.value(),
                quantity=self.input_quantity.value(),
                quantity_min=self.input_min_quantity.value(),
                quantity_store=self.input_store_quantity.value(),
                ed=self.ed_izm.text(),
                id_m=self.material_data[0]
            )
            self.submit_success.emit()
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