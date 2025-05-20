import secrets
import psycopg2
from database import connect_to_db
import bcrypt


class User:
    secret_key = secrets.token_hex(32)
    token_user =''

    def __init__(self, username, email, password_hash, role='user', user_id=None):
        self.id = user_id  # optionnel
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role

    @classmethod
    def hash_password(cls, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def get_connection(self):
        conn = connect_to_db()
        if conn is None:
            raise ConnectionError("Could not connect to the database.")
        return conn

    def create_user(self, admin_role='admin'):
        # Seuls les admins peuvent créer un utilisateur, donc on vérifie

        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users (username, email, password, role)
                VALUES (%s, %s, %s, %s)
            """, (self.username, self.email, self.password_hash, self.role))
            conn.commit()
            print(f"✅ User '{self.username}' created.")
        except Exception as e:
            print("❌ Error while creating user:", e)
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @classmethod
    def get_all_users(cls, admin_role='admin'):
        # Exemple : la méthode peut être appelée sans instance, donc on doit passer un paramètre role admin en argument
        # Si tu veux gérer les droits mieux, fais une classe AdminUser séparée ou un paramètre explicite
        conn = None
        cur = None
        users = []
        try:
            conn = connect_to_db()
            if conn is None:
                raise ConnectionError("Could not connect to the database.")
            cur = conn.cursor()
            cur.execute("SELECT id, username, email, password, role FROM users")
            rows = cur.fetchall()
            for row in rows:
                user = cls(username=row[1], email=row[2], password_hash=row[3], role=row[4], user_id=row[0])
                users.append(user)
            return users
        except Exception as e:
            print("❌ Error while fetching users:", e)
            return []
        finally:
            if cur: cur.close()
            if conn: conn.close()

    def update_user(self, admin_role='admin'):
        if self.role != admin_role:
            raise PermissionError("Only admins can update users.")

        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE users SET
                    email = %s,
                    password = %s,
                    role = %s
                WHERE username = %s
            """, (self.email, self.password_hash, self.role, self.username))
            conn.commit()
            if cur.rowcount:
                print(f"✅ User '{self.username}' updated.")
            else:
                print("⚠️ User not found.")
        except Exception as e:
            print("❌ Error while updating user:", e)
        finally:
            if cur: cur.close()
            if conn: conn.close()

    def delete_user(self, admin_role='admin'):
        if self.role != admin_role:
            raise PermissionError("Only admins can delete users.")

        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE username = %s", (self.username,))
            conn.commit()
            if cur.rowcount:
                print(f"✅ User '{self.username}' deleted.")
            else:
                print("⚠️ User not found.")
        except Exception as e:
            print("❌ Error while deleting user:", e)
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @classmethod
    def find_by_email(cls, email):
        conn = None
        cur = None
        try:
            conn = connect_to_db()
            if conn is None:
                raise ConnectionError("Could not connect to the database.")
            cur = conn.cursor()
            cur.execute("SELECT id, username, email, password, role FROM users WHERE email = %s", (email,))
            row = cur.fetchone()
            if row:
                return cls(username=row[1], email=row[2], password_hash=row[3], role=row[4], user_id=row[0])
            return None
        except Exception as e:
            print("❌ Error while fetching user by email:", e)
            return None
        finally:
            if cur: cur.close()
            if conn: conn.close()

##############################################################################################################
class Book:
    def __init__(self, title, author, description, owner_id, book_id=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.owner_id = owner_id

    def get_connection(self):
        conn = connect_to_db()
        if conn is None:
            raise ConnectionError("Could not connect to the database.")
        return conn

    def save(self):
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO books (title, author, description, owner_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (self.title, self.author, self.description, self.owner_id))
            self.id = cur.fetchone()[0]
            conn.commit()
            print(f"✅ Book '{self.title}' added with ID {self.id}.")
        except Exception as e:
            print("❌ Error while saving book:", e)
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @classmethod
    def get_all(cls):
        conn = None
        cur = None
        books = []
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT id, title, author, description, owner_id FROM books")
            rows = cur.fetchall()
            for row in rows:
                books.append(cls(row[1], row[2], row[3], row[4], book_id=row[0]))
            return books
        except Exception as e:
            print("❌ Error while fetching books:", e)
            return []
        finally:
            if cur: cur.close()
            if conn: conn.close()


#########################################################################################

class Review:
    def __init__(self, rating, comment, user_id, book_id, review_id=None):
        self.id = review_id
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.book_id = book_id

    def get_connection(self):
        conn = connect_to_db()
        if conn is None:
            raise ConnectionError("Could not connect to the database.")
        return conn

    def save(self):
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO reviews (rating, comment, user_id, book_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (self.rating, self.comment, self.user_id, self.book_id))
            self.id = cur.fetchone()[0]
            conn.commit()
            print(f"✅ Review added with ID {self.id}.")
        except Exception as e:
            print("❌ Error while saving review:", e)
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @classmethod
    def get_reviews_for_book(cls, book_id):
        conn = None
        cur = None
        reviews = []
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute("""
                SELECT id, rating, comment, user_id, book_id
                FROM reviews WHERE book_id = %s
            """, (book_id,))
            rows = cur.fetchall()
            for row in rows:
                reviews.append(cls(row[1], row[2], row[3], row[4], review_id=row[0]))
            return reviews
        except Exception as e:
            print("❌ Error while fetching reviews:", e)
            return []
        finally:
            if cur: cur.close()
            if conn: conn.close()
