from db.conn import connect_to_db


class User:
    def __init__(self, user_id=None, name=None, email=None, password=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def create(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (self.name, self.email, self.password)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_all():
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users")
            item_data = cursor.fetchall()
            products = []  # Lista para almacenar los objetos Item
            for row in item_data:
                # Crear un objeto Item con cada fila de datos
                product = User(*row)
                products.append(product)
            return products  # Devolver la lista de objetos Item
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

        # Método para obtener un ítem de la base de datos por su ID

    @staticmethod
    def read(user_id):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM users WHERE user_id = %s", (user_id,))
            product_data = cursor.fetchone()
            if product_data:
                product = User(*product_data)
                return product
            else:
                return None
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

        # Método para actualizar un ítem en la base de datos

    def update(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE users SET name = %s, email = %s, password = %s WHERE user_id = %s",
                (self.name, self.email, self.password, self.user_id)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

        # Método para eliminar un ítem de la base de datos por su ID

    @staticmethod
    def delete(user_id):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def read_by_email(email):
        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user_data = cursor.fetchone()
            if user_data:
                user = User(*user_data)
                return user
            else:
                return None
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()
