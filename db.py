import sqlite3
DATABASE_NAME = "students.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    try:
        tables = ["""CREATE TABLE students (sid INTEGER, first_name TEXT, last_name TEXT, dob TEXT, amount_due TEXT)"""]
        db = get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
        print("Table Created Successful!")
    except:
        print("Table Already Exist!")
