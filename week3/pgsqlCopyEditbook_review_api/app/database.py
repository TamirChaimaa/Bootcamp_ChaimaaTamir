import psycopg2
from psycopg2 import OperationalError, Error

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="Library",
            user="postgres",
            password="admin",
            port="5432"
        )
        print("✅ Connected to PostgreSQL database")
        return connection

    except OperationalError as e:
        print("❌ Operational error while connecting to the database:", e)
    except Error as e:
        print("❌ General database error:", e)
    except Exception as e:
        print("❌ Unexpected error:", e)

    return None

