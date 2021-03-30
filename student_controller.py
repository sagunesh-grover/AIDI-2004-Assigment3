from db import get_db


def insert_student(sid, first_name, last_name, dob, amount_due):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO students (sid, first_name, last_name, dob, amount_due) VALUES (?,?,?,?,?)"
    cursor.execute(statement, [sid,first_name,last_name,dob,amount_due])
    db.commit()
    return True


def update_student(sid, first_name, last_name, dob, amount_due):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE students SET first_name = ?, last_name = ?, dob = ?, amount_due = ? WHERE sid = ?"
    cursor.execute(statement, [first_name, last_name, dob, amount_due, sid])
    db.commit()
    return True


def delete_student(sid):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM students WHERE sid = ?"
    cursor.execute(statement, [sid])
    db.commit()
    return True


def get_by_sid(sid):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT sid, first_name, last_name, dob, amount_due FROM students WHERE sid = ?"
    cursor.execute(statement, [sid])
    return cursor.fetchone()


def get_students():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT sid, first_name, last_name, dob, amount_due FROM students"
    cursor.execute(query)
    return cursor.fetchall()
