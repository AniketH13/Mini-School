import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from models.attendance import Attendance

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("attendance_list"))


@app.route("/attendance", methods=["GET"])
def attendance_list():
    records = Attendance.get_all()
    return render_template("attendance.html", records=records)


@app.route("/attendance/add", methods=["POST"])
def add_attendance():
    date = request.form["date"]
    student_name = request.form["student_name"]
    status = request.form["status"]

    Attendance.create(date, student_name, status)
    return redirect(url_for("attendance_list"))


if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
DATABASE = "school.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    db = get_db()
    attendance = db.execute(
        "SELECT date, student_name, status FROM attendance"
    ).fetchall()

    return render_template("home.html", attendance=attendance)


if __name__ == "__main__":
    app.run(debug=True)
