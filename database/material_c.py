from mysql.connector import connect


def material_rash(
        id_product: int,
        id_type_material: int,
        quantity_materials: int,
        product_parameter_one: float,
        product_parameter_two: float
):
    """
        Функция рассчитывающая целое количество получаемой продукции
        из заданного количества сырья, учитывая потери сырья
    """

    try:
        conn = connect(
            host="127.0.0.1",
            database="furniture_db",
            user="root",
            password="toor"
        )

        cursor = conn.cursor()
        cursor.execute(
            "SELECT pt.coef FROM ProductType AS pt WHERE pt.id_product_type=(SELECT id_type_production FROM Product WHERE id_product=%s)",
            (id_product,))
        product_type_data = cursor.fetchone()
        cursor.close()

        cursor = conn.cursor()
        cursor.execute("SELECT procent FROM MaterialType AS mt WHERE mt.id_type_material=%s", (id_type_material,))
        material_type_data = cursor.fetchone()
        cursor.close()

        result: float = product_parameter_one * product_parameter_two * product_type_data[0] * material_type_data[0]
        return result
    except Exception:
        return -1