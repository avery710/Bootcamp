from flask import Flask, redirect, render_template, request, url_for, session, jsonify, g
from flask_session import Session
import mysql.connector


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


# @app.before_first_request
# def before_first_request():
dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "angeldemima0710",
    "database" : "member_sys"
}

# configure the connection pool in the global object
cnx_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "mysql_pool",
    pool_size = 10,
    autocommit = True,
    **dbconfig
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=["POST"])
def signup():
    # try:
    #     my_db = mysql.connector.connect(
    #         host = "localhost",
    #         user = "root",
    #         password = P,
    #         database = "member_sys"
    #     )
    #     my_cursor = my_db.cursor()

    connection = cnx_pool.get_connection()
    my_cursor = connection.cursor()

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
            return redirect(url_for('index'))
    # finally:
    #     my_cursor.close()
    #     my_db.close()


@app.route("/signin", methods=["POST"])
def signin():
    # try:
    #     my_db = mysql.connector.connect(
    #         host = "localhost",
    #         user = "root",
    #         password = P,
    #         database = "member_sys"
    #     )
    #     my_cursor = my_db.cursor()

    connection = cnx_pool.get_connection()
    my_cursor = connection.cursor()

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
    # finally:
    #     my_cursor.close()
    #     my_db.close()


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/member")
def member():
    if not session.get("name") and not session.get("id"):
        return redirect(url_for('index'))

    # try:
    #     my_db = mysql.connector.connect(
    #         host = "localhost",
    #         user = "root",
    #         password = P,
    #         database = "member_sys"
    #     )
    #     my_cursor = my_db.cursor()

    connection = cnx_pool.get_connection()
    my_cursor = connection.cursor()

    return render_template("member.html", name=session['name'])
    # finally:
    #     my_cursor.close()
    #     my_db.close()
    

@app.route("/api/member", methods=["GET", "PATCH"])
def fetch_api():
    if request.method == "GET":
        username = request.args.get("username")

        if (username):
            # try:
            #     my_db = mysql.connector.connect(
            #         host = "localhost",
            #         user = "root",
            #         password = P,
            #         database = "member_sys"
            #     )
            #     my_cursor = my_db.cursor()

            connection = cnx_pool.get_connection()
            my_cursor = connection.cursor()

            select_user = (
                "SELECT ID, name FROM member "
                "WHERE username = %s"
            )

            my_cursor.execute(select_user, (username,))
            user = my_cursor.fetchone()

            if (user and session['id']):
                response = {
                    "data" : {
                        "id" : user[0], 
                        "name" : user[1], 
                        "username": username
                    }
                }
                return jsonify(response)      
            else:
                response = {
                    "data" : None
                }
                return jsonify(response)
            # finally:
            #     my_cursor.close()
            #     my_db.close()

    if request.method == "PATCH":
        new_name = None
        # get data from request
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            new_name = json['name']
        else:
            return 'Content-Type not supported!'

        # query mySQL database and update the name
        # try:
        #     my_db = mysql.connector.connect(
        #         host = "localhost",
        #         user = "root",
        #         password = P,
        #         database = "member_sys"
        #     )
        #     my_cursor = my_db.cursor()

        connection = cnx_pool.get_connection()
        my_cursor = connection.cursor()

        if session['id']:
            # update the name
            update_name = (
                "UPDATE member "
                "SET name = %s "
                "WHERE ID = %s"
            )

            my_cursor.execute(update_name, (new_name, session['id']))

            # send response back
            res = {
                    "ok": True
            }
            return jsonify(res)

        else:  
            res = {
                "error": False
            }
            return jsonify(res)
            
        # finally:
        #     my_cursor.close()
        #     my_db.close()

        
@app.route("/signout")
def signout():
    session["name"] = None
    session["id"] = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)