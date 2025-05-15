# menu_item.py
# menu_item.py

import psycopg2
from psycopg2 import OperationalError

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @staticmethod
    def connect():
        """Méthode privée pour créer une connexion à la base."""
        try:
            conn = psycopg2.connect(
                dbname="Menu",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            return conn
        except OperationalError as e:
            print("Erreur de connexion :", e)
            return None


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
        print(f"L'élément '{self.name}' a été ajouté à la base.")


    def delete(self):
        conn = MenuItem.connect()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"L'élément '{self.name}' a été supprimé de la base.")
    
    
    def update(self, new_name=None, new_price=None):
        conn = MenuItem.connect()
        if conn is None:
            return
        cursor = conn.cursor()

        # On garde l'ancien nom pour la requête WHERE
        old_name = self.name

        if new_name:
            self.name = new_name

        if new_price is not None:
            self.price = new_price

        # Mise à jour des deux champs en une requête
        cursor.execute(
            "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
            (self.name, self.price, old_name)
        )

        conn.commit()
        cursor.close()
        conn.close()
        print(f"L'élément a été mis à jour : {self.name} - {self.price} €")

if __name__ == "__main__":
    # Ajouter un élément
   item = MenuItem('Burger', 35)
   item.save()
   item.delete()
   item.update('Veggie Burger', 37)
