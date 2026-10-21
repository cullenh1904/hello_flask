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

@app.route("/menu/<int:food_id>")
def food_detail(food_id):
    ingredient_data =query_db( """SELECT food_ingredients.ingredient_id, ingredients.ingredient_name
         FROM food_ingredients 
         JOIN ingredients ON ingredients.ingredient_id = food_ingredients.ingredient_id
         WHERE ingredients.ingredient_id = ?""")
    return render_template("food_detail.html", ingredient_data=ingredient_data)

if __name__ == "__main__":
    app.run(debug=True)