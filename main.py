import sys
from PySide6 import QtWidgets

from src.db.db_worker import DBWorker
from src.db.load_data import load_data_from_files
from src.ui.pages.MainPage import MainWindow
from src.settings import SettingsApp


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    db = DBWorker()

    # Скрипт по загрузке данных в БД
    # loader = load_data_from_files(db)

    widget = MainWindow()
    widget.setWindowTitle(SettingsApp.APP_TITLE)
    widget.resize(SettingsApp.APP_WIDTH, SettingsApp.APP_HEIGH)
    widget.show()

    sys.exit(app.exec())