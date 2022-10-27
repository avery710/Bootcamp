from crypt import methods
from flask import Flask, redirect, render_template, request, url_for, session
from flask_session import Session
import mysql.connector
from mysql.connector import errorcode


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/signup", methods=["POST"])
def signup():
    try:
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "member_sys"
        )
        my_cursor = my_db.cursor()

        if request.method == "POST":
            name = request.form.get('name')
            username = request.form.get("username")
            password = request.form.get("password")

            query = "SELECT username FROM member WHERE username = %s"
            my_cursor.execute(query, (username,))
            result = my_cursor.fetchone()

            if (result):
                return redirect(url_for('error', message="帳號已經被註冊"))
            else:
                insert_new_member = (
                    "INSERT INTO member (name, username, password) "
                    "VALUES (%s, %s, %s)")
                
                my_cursor.execute(insert_new_member, (name, username, password))
                my_db.commit()
                return redirect(url_for('index'))
    finally:
        my_cursor.close()
        my_db.close()


@app.route("/signin", methods=["POST"])
def signin():
    try:
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "member_sys"
        )
        my_cursor = my_db.cursor()

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            query = (
                "SELECT id, name, username, password FROM member " 
                "WHERE username = %s AND password = %s")
            my_cursor.execute(query, (username, password))
            result = my_cursor.fetchone()

            if (result):
                session['id'] = result[0]
                session['name'] = result[1]

                return redirect(url_for('member'))        
            else:
                return redirect(url_for('error', message="帳號或密碼輸入錯誤"))
    finally:
        my_cursor.close()
        my_db.close()


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/member")
def member():
    if not session.get("name") and not session.get("id"):
        return redirect(url_for('index'))

    try:
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "member_sys"
        )
        my_cursor = my_db.cursor()

        select_all_message = (
            "SELECT name, content FROM message"
        )
        my_cursor.execute(select_all_message)

        messages = []

        for name, content in my_cursor:
            messages.append((name, content))

        return render_template("member.html", name=session['name'], messages=messages)
    finally:
        my_cursor.close()
        my_db.close()
    

@app.route("/signout")
def signout():
    session["name"] = None
    session["id"] = None
    return redirect(url_for('index'))


@app.route("/message", methods=["POST"])
def message():
    try:
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "member_sys"
        )
        my_cursor = my_db.cursor()

        id = session['id']
        name = session['name']
        content = request.form.get('content')

        insert_message = (
            "INSERT INTO message (member_id, name, content) "
            "VALUES (%s, %s, %s)"
        )

        my_cursor.execute(insert_message, (id, name, content))
        my_db.commit()

        return redirect(url_for('member'))
    finally:
        my_cursor.close()
        my_db.close()


if __name__ == '__main__':
    app.run(debug=True)