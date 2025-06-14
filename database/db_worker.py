from mysql.connector import connect
from src.settings import SettingsApp

class DBWorker:
    def __init__(self):
        self.connect = connect(
            host=SettingsApp.host,
            database=SettingsApp.database,
            user=SettingsApp.user,
            password=SettingsApp.password
        )

        self.create_tables()

    def create_tables(self):
        """
        Создание таблиц и отношений между ними
        :return:
        """

        cursor = self.connect.cursor()

        tables: list[str] = [
            """
                CREATE TABLE IF NOT EXISTS MaterialType (
                    id_type_material INT PRIMARY KEY AUTO_INCREMENT,
                    name_material VARCHAR(200),
                    procent VARCHAR(8)
                );
            """,
            """
                CREATE TABLE IF NOT EXISTS ProductType (
                    id_product_type INT PRIMARY KEY AUTO_INCREMENT,
                    name_product_type VARCHAR(125),
                    coef DECIMAL(10, 2)
                );
            """,
            """
                CREATE TABLE IF NOT EXISTS Material (
                    id_material INT PRIMARY KEY AUTO_INCREMENT,
                    name_material VARCHAR(255),
                    id_type_material INT,
                    price DECIMAL(10, 2),
                    quantity INT,
                    min_quantity INT,
                    quanity_in_yp INT,
                    ed VARCHAR(30),
                    FOREIGN KEY (id_type_material) REFERENCES MaterialType(id_type_material)
                );
            """,
            """
                CREATE TABLE IF NOT EXISTS Product (
                    id_product INT PRIMARY KEY AUTO_INCREMENT,
                    name_product VARCHAR(325),
                    id_type_production INT,
                    article DECIMAL(20, 1),
                    min_price DECIMAL(10, 2),
                    FOREIGN KEY (id_type_production) REFERENCES ProductType(id_product_type)
                );
            """,
            """
                CREATE TABLE IF NOT EXISTS MaterialProduct (
                    id_material_product INT PRIMARY KEY AUTO_INCREMENT,
                    id_material INT,
                    id_product INT,
                    count INT,
                    FOREIGN KEY (id_material) REFERENCES Material(id_material),
                    FOREIGN KEY (id_product) REFERENCES Product(id_product)
                );
            """,
        ]

        for table in tables:
            cursor.execute(table)

        self.connect.commit()
        cursor.close()

    def get_all_materials(self):
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT m.id_material, m.name_material, m.id_type_material, m.price, m.quantity, m.min_quantity, m.quanity_in_yp, m.ed, mt.name_material, SUM(mp.count) FROM Material AS m LEFT JOIN MaterialType AS mt ON m.id_type_material = mt.id_type_material LEFT JOIN MaterialProduct AS mp ON mp.id_material = m.id_material GROUP BY m.id_material")
        all_materials = self.cursor.fetchall()
        self.cursor.close()

        return all_materials

    def get_all_material_type(self):
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM MaterialType")
        all_material_type = self.cursor.fetchall()

        self.cursor.close()
        return all_material_type

    def update_material_data(self, name_material: str, id_type_material: int, price: float, quantity: int, quantity_min: int, quantity_store: int, ed: str, id_m: int) -> bool:
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute(
                "UPDATE Material SET name_material=%s, id_type_material=%s, price=%s, quantity=%s, min_quantity=%s, quanity_in_yp=%s, ed=%s WHERE id_material = %s",
                (name_material, id_type_material, price, quantity, quantity_min, quantity_store, ed, id_m)
            )
            self.connect.commit()
            self.cursor.close()
            return True
        except Exception:
            return False

    def add_material(self, name_material: str, id_type_material: int, price: float, quantity: int, quantity_min: int, quantity_store: int, ed: str) -> bool:
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute(
                "INSERT INTO Material (name_material, id_type_material, price, quantity, min_quantity, quanity_in_yp, ed) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name_material, id_type_material, price, quantity, quantity_min, quantity_store, ed)
            )
            self.connect.commit()
            self.cursor.close()
            return True
        except Exception:
            return False

    def get_all_products(self, id_material: int) -> list:
        try:
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT p.id_product, p.name_product, p.article, p.min_price, pt.name_product_type, SUM(mt.count) FROM Product AS p LEFT JOIN MaterialProduct AS mt ON p.id_product = mt.id_product AND mt.id_material = %s INNER JOIN ProductType AS pt ON pt.id_product_type = p.id_type_production GROUP BY p.id_product", (id_material, ))
            result = self.cursor.fetchall()
            self.cursor.close()
            return result
        except Exception as ex:
            return []