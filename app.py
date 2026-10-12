from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():  #test
    db = sqlite3.connect("food.db")
    cursor = db.cursor()
    sql = ("""SELECT food_id
            FROM foods
            """)
    cursor.execute(sql)
    results = cursor.fetchall()

if __name__ == '__main__':
    app.run(debug=True)