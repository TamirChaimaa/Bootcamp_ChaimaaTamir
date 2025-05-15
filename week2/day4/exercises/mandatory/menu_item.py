import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="restaurant",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                (self.name, self.price)
            )
            conn.commit()
            print(f"Item '{self.name}' added successfully.")
        except Exception as e:
            print("Error while saving item:", e)
        finally:
            cur.close()
            conn.close()

    def delete(self):
        try:
            conn = get_connection()
            cur = conn.cursor()

            # Vérifie si l'item existe dans la base
            cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (self.name,))
            item = cur.fetchone()

            if not item:
                print(f"Error: Item '{self.name}' does not exist. Deletion cancelled.")
                return

            # L'item existe, donc on le supprime
            cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
            conn.commit()
            print(f"Item '{self.name}' deleted successfully.")

        except Exception as e:
            print("Error while deleting item:", e)
        finally:
            cur.close()
            conn.close()

    def update(self, new_name, new_price):
        try:
            conn = get_connection()
            cur = conn.cursor()

            # Vérifie si l'item existe avant de le mettre à jour
            cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (self.name,))
            item = cur.fetchone()

            if not item:
                print(f"Error: Item '{self.name}' does not exist. Update cancelled.")
                return

            cur.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                (new_name, new_price, self.name)
            )
            conn.commit()
            print(f"Item '{self.name}' updated successfully.")

        except Exception as e:
            print("Error while updating item:", e)
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    # create_table = f'''
    #             CREATE TABLE Menu_Items(
    #                 item_id SERIAL PRIMARY KEY,
    #                 item_name VARCHAR(30) NOT NULL,
    #                 item_price SMALLINT DEFAULT 0
    #             )
    #             '''
    
    item = MenuItem('Burger', 35)
    item.save()
    # item.delete()
    item.update('Veggie Burgy', 37)