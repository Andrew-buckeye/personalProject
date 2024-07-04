# importing redirect
from flask import Flask, redirect, url_for, render_template, request
from mfa import emailSender
# Initialize the flask application

app = Flask(__name__)

# It will load the form template which
# is in login.html
@app.route('/')
def index():
    return render_template("login.html")

# loggning to the form with method POST or GET
@app.route("/login", methods=["POST", "GET"])
def login():
    # if the method is POST and Username is admin then
    # it will redirects to success url.
    if request.method == "POST" and request.form["username"] == "admin":
        return redirect(url_for("success"))
    if request.method == "POST" and request.form["username"] == "user":
        return redirect(url_for("mfa"))

    # if the method is GET or username is not admin,
    # then it redirects to index method.
    return redirect(url_for('index'))


@app.route("/mfa", methods=["POST", "GET"])
def mfa():
    if request.method == "POST" and request.form["username"] == "num":
        num = emailSender()
        print(num)
        print("got it")
        return redirect(url_for("success"))
    return render_template("mfa.html")



@app.route('/profile')
def profile():
     return render_template("profile.html")
@app.route('/success')
def success():
     return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)