from flask import Flask, request, redirect, url_for, session, render_template_string, flash, render_template
from flask_session import Session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a secure random key in production
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DB_NAME = 'users.db'

# Initialize DB
def init_db_and_users_tbl():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')


# def prep_book_db():
#     with sqlite3.connect(DB_NAME) as conn:
#         conn.execute('''DROP TABLE IF EXISTS books''')
# prep_book_db()


def init_books_tbl():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_title TEXT UNIQUE NOT NULL,
                book_author TEXT
            )
        ''')

def init_games_tbl():
    with sqlite3.connect("gaming.db") as conn:
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS games (
                        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        game_tite TEXT UNIQUE NOT NULL,
                        year INTEGER NOT NULL
                     )''')

# def check_tbl():
#     with sqlite3.connect("users.db") as conn:
#         conn.execute('''SELECT name FROM sqlite_master
#                      ''')
#     # with sqlite3.connect("gaming.db") as conn:
#     #     conn.execute('''SELECT name FROM sqlite_master
#     #                  ''')


init_db_and_users_tbl()
init_books_tbl()
init_games_tbl()

# Register
@app.route('/', methods=['GET'])
def index():
    return redirect("/login")

def generate_custom_id(prefix="user", chosen_db="users.db", chosen_tbl="users"):
    padding=3
    with sqlite3.connect(chosen_db) as conn:
        cur = conn.cursor()
        sql_query = f"SELECT COUNT(*) FROM {chosen_tbl}"
        cur.execute(sql_query)
        count = cur.fetchone()[0] + 1
        return f"{prefix}_{str(count).zfill(padding)}"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        custom_id = generate_custom_id(prefix="user", chosen_db="users.db", chosen_tbl="users")
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute('INSERT INTO users (username, password, new_id) VALUES (?, ?, ?)', (username, password, custom_id))
            flash("User registered successfully!", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.", "error")
    return render_template("register.html")

@app.route('/register_book', methods=['GET', 'POST'])
def register_book():
    if request.method == "POST":
        book_title = request.form['book_title'].strip()
        book_author = request.form['book_author'].strip()
        print(book_title, book_author)
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute('INSERT INTO books (book_title, book_author) VALUES (?,?)', (book_title, book_author))
            flash("Book registered!")
            return redirect(url_for('register_book'))
        except sqlite3.IntegrityError:
            flash("Book already exists!", "error")
    return render_template("register_book.html")

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == "POST":
        game_title  = request.form['game_title'].strip()
        year        = request.form['year'].strip()
        print(game_title, year)
        try:
            with sqlite3.connect("gaming.db") as conn:
                conn.execute('INSERT INTO games (game_title, year) VALUES (?,?)', (game_title, year))
            flash("Game registered!")
            return redirect(url_for('add_game'))
        except sqlite3.IntegrityError:
            flash("Game already exists!", "error")
    return render_template("add_game.html")

@app.route('/games_list')
def games_list():
    with sqlite3.connect("gaming.db") as conn:
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM games").fetchall()
        print(f"games_list: {res}")
    return render_template("games_list.html", games_list=res)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        with sqlite3.connect(DB_NAME) as conn:
            user = conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password)).fetchone()
            if user:
                session['username'] = username
                print(session['username'])
                # flash("Logged in successfully!", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials", "error")
    return render_template("login.html")

# Dashboard
@app.route('/dashboard', methods=["GET","POST"])
def dashboard():
    if 'username' not in session or not session['username']:
        return redirect(url_for('login'))

    flash("Logged in successfully!", "success")

    with sqlite3.connect(DB_NAME) as conn:
        books = conn.execute('SELECT book_id, book_title, book_author FROM books').fetchall()
        users = conn.execute('SELECT id, username FROM users').fetchall()

    user_cart_key = f"cart_{session['username']}"
    print(f"user_cart_key: {user_cart_key}")
    if request.method == "POST":
        book_id = request.form.get("book_id")
        game_id = request.form.get("game_id")
        if request.form.get("action") == "add":
            # create user cart_key
            if user_cart_key not in session:
                session[user_cart_key] = []
            session[user_cart_key].append(book_id)
        elif request.form.get("action") == "remove":
            session[user_cart_key].remove(book_id)
    # books_in_cart = session["cart"]
    # print(f"books_in_cart: {books_in_cart}")
    # return render_template("cart.html", books_in_cart = books_in_cart)

    if user_cart_key not in session:
        session[user_cart_key] = []
    books_in_cart = session[user_cart_key]
    print(f"books_in_cart: {books_in_cart}") # books_in_cart: ['1']
    # print(f"books: {books}") # 
    
    # with sqlite3.connect(DB_NAME) as conn:
    #     cur = conn.cursor()
    #     books_in_cart_sql = cur.execute('SELECT book_title FROM books WHERE books_id in ?',(books_in_cart)).fetchall()

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        query = f"SELECT book_id, book_title FROM books WHERE book_id IN ({','.join(['?'] * len(books_in_cart))})"
        books_list_of_tuples = cur.execute(query, books_in_cart).fetchall()
    
    print(f"books_in_cart_sql: {books_list_of_tuples}, {type(books_list_of_tuples)}")

    # with sqlite3.connect(DB_NAME) as conn:
    #     cur = conn.cursor()
    #     placeholders = ','.join(['?'] * len(books_in_cart))
    #     query = f'''
    #         SELECT book_id, book_title, book_author 
    #         FROM books 
    #         WHERE book_id IN ({placeholders})
    #     '''
    #     books_in_cart_sql = cur.execute(query, tuple(books_in_cart)).fetchall()

    [print(f'k:[{k}], v:[{v}]') for k,v in session.items()]
    # return render_template("dashboard.html", users=users, books=books, books_in_cart=books_in_cart)
    
    # games_list
    with sqlite3.connect("gaming.db") as conn:
        cur = conn.cursor()
        games_list = cur.execute("SELECT * FROM games").fetchall()
        print(f"games_list: {games_list}")

    return render_template("dashboard.html", 
                           users=users, 
                           books=books, 
                           books_in_cart=books_list_of_tuples,
                           games_list=games_list)

# Delete User
@app.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    if 'username' not in session or not session['username']:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM users WHERE id=? AND username != ?', (user_id, session['username']))
    flash("User deleted (if not yourself).", "success")
    return redirect(url_for('dashboard'))

@app.route('/cart', methods=["GET","POST"])
def cart():
    if request.method == "POST":
        book_id = request.form.get("book_id")
        if request.form.get("action") == "add":
            if "cart" not in session:
                session["cart"] = []
            session["cart"].append(book_id)
        elif request.form.get("action") == "remove":
            session["cart"].remove(book_id)
    books_in_cart = session["cart"]
    print(f"books_in_cart: {books_in_cart}")
    return render_template("cart.html", books_in_cart = books_in_cart)

@app.route('/clear_cart')
def clear_cart():
    user_cart_key = f"cart_{session['username']}"
    session[user_cart_key] = []
    # return redi
    # rect(url_for('cart'))
    return redirect(url_for('dashboard'))

    
# Logout
@app.route('/logout')
def logout():
    # session.clear()
    session['username'] = None
    print(session['username'])
    return redirect(url_for('login'))

# Run app
if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
