from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def menu():
    db = sqlite3.connect("food.db")
    cursor = db.cursor()
    sql = ("""SELECT food_id FROM foods""")
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("menu.html",results=results)

if __name__ == "__main__":
    app.run(debug=True)