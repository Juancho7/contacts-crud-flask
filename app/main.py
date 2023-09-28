from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor

app = Flask(__name__)

app.secret_key = "your secret key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "*Mysql*Root*7"
app.config["MYSQL_DB"] = "flask_basics"

mysql = MySQL(app)


@app.route("/")
def index():
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT * FROM contacts")
    contacts_data = cursor.fetchall()
    cursor.close()
    print(contacts_data)
    return render_template("index.html", contacts=contacts_data)


@app.route("/add", methods=["POST"])
def add_contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]
        print(fullname, phone, email, "Prueba")
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)",
                (fullname, phone, email),
            )
            mysql.connection.commit()
            return redirect(url_for("index"))
        except Exception as e:
            raise e

    return "Add contact"


@app.route("/edit")
def edit_contact():
    return "Edit contact"


@app.route("/delete")
def delete_contact():
    return "Delete contact"


if __name__ == "__main__":
    app.run(debug=True)
