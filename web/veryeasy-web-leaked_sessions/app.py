from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import secrets
import os

app = Flask(__name__)

DB = "sessions.db"
ADMIN_FLAG = "shellmates{9571c5bd902f38d46662cdd2fb}"
SESSIONS = {} 

admin_session_id = secrets.token_hex(16)
SESSIONS[admin_session_id] = "admin"

def init_db():
    if os.path.exists(DB):
        os.remove(DB)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL,
           is_admin INTEGER NOT NULL DEFAULT 0
       )
    """)
    admin_pass = secrets.token_hex(8)
    hashed = generate_password_hash(admin_pass)
    cur.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES (?, ?, 1)", ("admin", hashed))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    conn.close()
    return user

def get_current_user():
    session_id = request.cookies.get("session_id")
    if not session_id:
        return None
    username = SESSIONS.get(session_id)
    if not username:
        return None
    return get_user_by_username(username)

@app.route("/")
def index():
    user = get_current_user()
    if user is None:
        return redirect(url_for("register"))
    return render_template("profile.html", user=user,flag=ADMIN_FLAG)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = get_user_by_username(username)

        if user is None or not check_password_hash(user["password"], password):
           error = "Invalid username or password."
        else:
            session_id = secrets.token_hex(16)
            SESSIONS[session_id] = username

            resp = make_response(redirect(url_for("index")))
            resp.set_cookie("session_id", session_id, httponly=True, samesite="Lax")
            return resp

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            error = "Username and password required."
        elif get_user_by_username(username):
            error = "Username already taken."
        else:
            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            hashed = generate_password_hash(password)
            cur.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, 0)",
                        (username, hashed))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
    return render_template("register.html", error=error)

@app.route("/login-infos")
def login_infos():
    user = get_current_user()
    if user is None:
        return redirect(url_for("login"))

    all_sessions = [{"session_id": sid, "username": uname} for sid, uname in SESSIONS.items()]
    return render_template("login_infos.html", user=user, sessions=all_sessions)

@app.route("/logout")
def logout():
    session_id = request.cookies.get("session_id")
    SESSIONS.pop(session_id, None)
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("session_id")
    return resp

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", debug=False, port=5055)