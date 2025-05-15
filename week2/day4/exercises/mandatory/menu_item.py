import psycopg2
from psycopg2 import OperationalError

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @staticmethod
    def connect():
        """Create a connection and ensure the table exists."""
        try:
            conn = psycopg2.connect(
                dbname="restaurant",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            # Dès qu'on a la connexion, on s'assure que la table existe
            MenuItem.create_table(conn)
            return conn
        except OperationalError as e:
            print("Connection error:", e)
            return None
        
    @staticmethod
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Menu_Items (
                item_id SERIAL PRIMARY KEY,
                item_name VARCHAR(100) UNIQUE NOT NULL,
                item_price NUMERIC(6, 2) NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        print("Table 'Menu_Items' is ready.")

    def save(self):
        conn = MenuItem.connect()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
            (self.name, self.price)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"The item '{self.name}' has been added to the database.")

    def delete(self):
        conn = MenuItem.connect()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"The item '{self.name}' has been deleted from the database.")
    
    def update(self, new_name=None, new_price=None):
        conn = MenuItem.connect()
        if conn is None:
            return
        cursor = conn.cursor()

        old_name = self.name

        if new_name:
            self.name = new_name

        if new_price is not None:
            self.price = new_price

        cursor.execute(
            "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
            (self.name, self.price, old_name)
        )

        conn.commit()
        cursor.close()
        conn.close()
        print(f"The item has been updated: {self.name} - {self.price} €")

if __name__ == "__main__":
    item = MenuItem('Burger', 35)
    item.save()
    item.delete()
    item.update('Veggie Burger', 37)
