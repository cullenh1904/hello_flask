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


if __name__ == '__main__':
    app.run(debug=True)