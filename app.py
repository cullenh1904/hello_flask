from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
database = "food.db"

def query_db(sql, args=(), one=False):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    cursor.execute(sql, args)
    results = cursor.fetchall()
    db.close()
    return (results[0] if results else None) if one else results

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/menu")
def menu():
    results = query_db("SELECT * FROM foods")
    return render_template("menu.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)