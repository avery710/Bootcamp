from crypt import methods
from flask import Flask, redirect, render_template, request, url_for, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return redirect(url_for('square', num=request.form.get('num')))
    return render_template('index.html')

@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return redirect(url_for('error', message="請輸入帳號、密碼"))
        elif username == "test" and password =="test":
            session["username"] = username
            return redirect(url_for('member'))
        elif username != "test" or password != "test":
            return redirect(url_for('error', message="帳號或密碼輸入錯誤"))


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)


@app.route("/member")
def member():
    if not session.get("username"):
        return redirect(url_for('index'))
    return render_template("member.html")
    

@app.route("/signout")
def signout():
    session["username"] = None
    return redirect(url_for('index'))


@app.route("/square/<int:num>")
def square(num):
    n = num * num
    return render_template("square.html", num=n)


if __name__ == '__main__':
    app.run(debug=True)