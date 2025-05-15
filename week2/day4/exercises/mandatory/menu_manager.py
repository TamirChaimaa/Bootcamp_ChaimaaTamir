from menu_item import get_connection, MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
            result = cur.fetchone()
            if result:
                return MenuItem(result[0], result[1])
            else:
                return None
        except Exception as e:
            print("Error fetching item:", e)
        finally:
            cur.close()
            conn.close()

    @classmethod
    def all_items(cls):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT item_name, item_price FROM Menu_Items")
            items = cur.fetchall()
            return [MenuItem(name, price) for name, price in items]
        except Exception as e:
            print("Error fetching all items:", e)
        finally:
            cur.close()
            conn.close()
if __name__ == "__main__":
    # item = MenuItem('Burger', 35)
    # item.save()
    # item.delete()
    # item.update('Veggie Burger', 37)
    item2 = MenuManager.get_by_name('Beef Stew')
    items = MenuManager.all()
    item2 = MenuManager.get_by_name('Veggie Burgy')
    print(item2)
    print(MenuManager.all_items())
