from flask import Flask, jsonify, request, render_template
import student_controller
import sqlite3 as sql
from db import create_tables,DATABASE_NAME

app = Flask(__name__)


@app.route('/')
def list():
    con = sql.connect(DATABASE_NAME)
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)


@app.route('/students', methods=["GET"])
def get_students():
    students = student_controller.get_students()
    return jsonify(students)


@app.route("/student", methods=["POST"])
def insert_student():
    student_details = request.get_json()
    sid = student_details["sid"]
    first_name = student_details["first_name"]
    last_name = student_details["last_name"]
    dob = student_details["dob"]
    amount_due = student_details["amount_due"]
    result = student_controller.insert_student(sid, first_name, last_name, dob, amount_due)
    return jsonify(result)


@app.route("/student", methods=["PUT"])
def update_student():
    student_details = request.get_json()
    sid = student_details["sid"]
    print(sid)
    first_name = student_details["first_name"]
    last_name = student_details["last_name"]
    dob = student_details["dob"]
    amount_due = student_details["amount_due"]
    result = student_controller.update_student(sid, first_name, last_name, dob, amount_due)
    return jsonify(result)




@app.route("/student/<sid>", methods=["DELETE"])
def delete_student(sid):
    result = student_controller.delete_student(sid)
    return jsonify(result)


@app.route("/student/<sid>", methods=["GET"])
def get_student_by_sid(sid):
    student = student_controller.get_by_sid(sid)
    return jsonify(student)




"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)
