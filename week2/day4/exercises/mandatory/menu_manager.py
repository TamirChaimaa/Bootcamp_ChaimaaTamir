import psycopg2
from psycopg2 import OperationalError
from menu_item import MenuItem  # Import the MenuItem class defined elsewhere

class MenuManager:

    @classmethod
    def connect(cls):
        """Private method to open a connection to the database."""
        try:
            conn = psycopg2.connect(
                dbname="restaurant",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            return conn
        except OperationalError as e:
            print("Connection error:", e)
            return None

    @classmethod
    def get_by_name(cls, name):
        conn = cls.connect()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s",
            (name,)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            item_name, item_price = result
            return MenuItem(item_name, item_price)
        else:
            return None

    @classmethod
    def all_items(cls):
        conn = cls.connect()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT item_name, item_price FROM Menu_Items")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [MenuItem(name, price) for name, price in rows]

if __name__ == "__main__":
    # Test get_by_name
    item = MenuItem('Burger', 35)
    item.save()
    item.update('Veggie Burger', 37)
    item2 = MenuManager.get_by_name('Beef Stew')
    items = MenuManager.all_items()
    
    print("Menu item list:")
    for item in items:
        print(f"Name: {item.name}, Price: {item.price} €")
