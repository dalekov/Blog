from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
import smtplib
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

API_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"

app = Flask(__name__)
app.secret_key = "your-secret-key-here"  # Replace with a strong random string

# Database setup
DB_PATH = "blog.db"


def init_db():
    """Initialize the database with users table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()


# Initialize the database when the app starts
init_db()


def get_db_connection():
    """Get a connection to the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn


# Get blog posts from API
all_posts = requests.get(url=API_ENDPOINT).json()


@app.route("/")
def index():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html", posts=all_posts)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        # Details for the emailing app
        my_email = "denisalekov17@gmail.com"
        my_password = "bfrr cwou ugoy kvab"

        # Send email with the relevant details:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="denis.alekov1@gmail.com",
                                msg=f"Subject: New blog contact!\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def show_post(index):
    selected_post = None
    for post in all_posts:
        if post.get('id') == index:
            selected_post = post
    return render_template('post.html', post=selected_post)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Connect to database
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        # Check if user exists and password matches
        if user and check_password_hash(user['password'], password):
            # Set session variables to track logged in user
            session['logged_in'] = True
            session['user_id'] = user['id']
            session['email'] = user['email']
            session['name'] = user['name']

            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        name = request.form.get('name', '')  # Optional name field

        # Validate form data
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return render_template('signup.html')

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Connect to database
        conn = get_db_connection()

        try:
            # Insert new user
            conn.execute(
                'INSERT INTO users (email, password, name) VALUES (?, ?, ?)',
                (email, hashed_password, name)
            )
            conn.commit()
            flash('Account created! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            # This happens if the email already exists
            flash('Email already registered. Please use a different email or login.', 'danger')
        finally:
            conn.close()

    return render_template('signup.html')


@app.route('/logout')
def logout():
    # Clear session data
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


# User profile route
@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        flash('Please log in to view your profile.', 'warning')
        return redirect(url_for('login'))

    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)