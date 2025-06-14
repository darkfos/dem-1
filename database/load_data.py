import os
import pandas as pnd
from typing import List, Any


def load_data_from_files(db) -> None:
    """
        Функция для внесения данных в таблицы из Excel
    """

    try:
        list_files: dict[str, str] = {
            "MaterialType": "Material_type_import.xlsx",
            "ProductType": "Product_type_import.xlsx",
            "Material": "Materials_import.xlsx",
            "Product": "Products_import.xlsx",
            "MaterialProduct": "Material_products__import.xlsx"
        }

        for file_name in list_files:
            for file_data in open_file(list_files.get(file_name)):

                cursor = db.connect.cursor()

                match file_name:
                    case "MaterialType":
                        cursor.execute(f"INSERT INTO MaterialType (name_material, procent) VALUES (%s, %s)",
                                       (file_data[0], file_data[1]))
                    case "ProductType":
                        cursor.execute(f"INSERT INTO ProductType (name_product_type, coef) VALUES (%s, %s)",
                                       (file_data[0], file_data[1]))
                    case "Material":
                        cursor_material_type = db.connect.cursor()
                        cursor_material_type.execute(
                            "SELECT * FROM MaterialType WHERE name_material=%s", (file_data[1],)
                        )

                        material_type = cursor_material_type.fetchone()
                        cursor_material_type.fetchall()

                        cursor_material_type.close()

                        if material_type:
                            file_data = list(file_data)
                            file_data[1] = material_type[0]
                            cursor.execute(
                                f"INSERT INTO Material (name_material, id_type_material, price, quantity, min_quantity, quanity_in_yp, ed) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                tuple(file_data))
                    case "Product":
                        cursor_product_type = db.connect.cursor()
                        cursor_product_type.execute(
                            "SELECT * FROM ProductType WHERE name_product_type=%s", (file_data[0],)
                        )

                        product_type_data = cursor_product_type.fetchone()
                        cursor_product_type.fetchall()

                        cursor_product_type.close()

                        if product_type_data:
                            cursor.execute(
                                "INSERT INTO Product (name_product, id_type_production, article, min_price) VALUES (%s, %s, %s, %s)",
                                (file_data[1], product_type_data[0], *file_data[2:])
                            )
                    case "MaterialProduct":

                        material_cursor = db.connect.cursor()
                        material_cursor.execute(
                            "SELECT * FROM Material WHERE name_material=%s", (file_data[0], )
                        )
                        material_data = material_cursor.fetchone()
                        material_cursor.fetchall()
                        material_cursor.close()

                        product_cursor = db.connect.cursor()
                        product_cursor.execute(
                            "SELECT * FROM Product WHERE name_product=%s", (file_data[1], )
                        )
                        product_data = product_cursor.fetchone()
                        product_cursor.fetchall()
                        product_cursor.close()

                        if material_data and product_data:
                            cursor.execute(
                                f"INSERT INTO MaterialProduct (id_material, id_product, count) VALUES (%s, %s, %s)",
                                (material_data[0], product_data[0], file_data[2]))

                db.connect.commit()
                cursor.close()
    except Exception as ex:
        print("Не удалось загрузить данные в БД.\nОшибка: {}".format(ex))

def open_file(file_name: str) -> List[Any]:
    """
        Функция-генератор для чтения файлов и отдачи части строк
    """

    with open(f"static/{file_name}", "rb") as file:

        excel_file = pnd.read_excel(file, header=None)
        for index, row in excel_file.iterrows():
            if index == 0:
                continue
            yield row.values