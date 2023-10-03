from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor

app = Flask(__name__)

app.secret_key = "your secret key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "flask_basics"

mysql = MySQL(app)


@app.route("/")
def index():
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT * FROM contacts")
    contacts_data = cursor.fetchall()
    cursor.close()
    return render_template("index.html", contacts=contacts_data)


@app.route("/add", methods=["POST"])
def add_contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]
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


@app.route("/edit/<id>", methods=["POST", "GET"])
def get_contact(id):
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (id,))
    contact_data = cursor.fetchone()
    cursor.close()
    print(contact_data)
    return render_template("edit-contact.html", contact=contact_data)


@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
    if request.method == "POST":
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s",
            (fullname, phone, email, id),
        )
        mysql.connection.commit()
        return redirect(url_for("index"))


@app.route("/delete/<id>", methods=["POST", "GET"])
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = %s", (id))
    mysql.connection.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
