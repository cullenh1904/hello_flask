from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    db = sqlite3.connect("game.db")
    cursor = db.cursor()
    sql = ("""SELECT id
            FROM game
            """)
    cursor.execute(sql)
    results = cursor.fetchall()
#---------------------------------------------------
    game_genre_dict = {}
    for search_game in results:
        sql = (f"""SELECT genre_id
                FROM game_genre
                WHERE game_id = {search_game[0]};
                """)
        cursor.execute(sql)
        search_game_genres = cursor.fetchall()
        game_genre_dict[search_game] = search_game_genres
#----------------------------------------------------
    display_list = []
    for i in game_genre_dict:
        sql = ("""SELECT name
            FROM game
            WHERE id = ?;
            """)
        cursor.execute(sql,(i))
        game_name = cursor.fetchall()
        temp_text = str(game_name[0][0])
        for j in game_genre_dict[i]:
            sql = ("""SELECT name
                FROM genre
                WHERE id = ?;
                """)
            cursor.execute(sql,(j))
            genre_name = cursor.fetchall()
            temp_text += " | "+str(genre_name[0][0])
        display_list.append(temp_text)
    return render_template('index.html', send_test = display_list)

@app.route("/awesome", methods=['GET', 'POST'])
def awesome():
    temp_text = ""
    search_game_genres = None
    # check if the user clicked on the submit button
    if request.method == 'POST':
        # retrieve data using the HTML 'name' attribute
        game = request.form.get("game_id")
        db = sqlite3.connect("game.db")
        cursor = db.cursor()
        sql = (f"""SELECT id FROM game WHERE name = '{game}';""")
        cursor.execute(sql)
        results = cursor.fetchall()

        sql = (f"""SELECT genre_id FROM game_genre WHERE game_id = {results[0][0]};""")
        cursor.execute(sql)
        search_game_genres = cursor.fetchall()
        for j in search_game_genres:
            sql = ("""SELECT name FROM genre WHERE id == ?;""")
            cursor.execute(sql,(j))
            genre_name = cursor.fetchall()
            temp_text += " | "+str(genre_name[0][0])
    return render_template('awesome.html', send_game = temp_text)

@app.route("/cool", methods=['GET', 'POST'])
def cool():
    temporary_text = ""
    if request.method == 'POST':
        temporary_text = request.form.get('my_textbox') 

    return render_template('cool.html', submitted_text=temporary_text)

if __name__ == '__main__':
    app.run(debug=True)