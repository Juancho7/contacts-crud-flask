from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "your secret key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "flask_basics"

mysql = MySQL(app)


@app.route("/")
def index():
    return "Hello world"


@app.route("/add")
def add_contact():
    return "Add contact"


@app.route("/edit")
def edit_contact():
    return "Edit contact"


@app.route("/delete")
def delete_contact():
    return "Delete contact"


if __name__ == "__main__":
    app.run(debug=True)
