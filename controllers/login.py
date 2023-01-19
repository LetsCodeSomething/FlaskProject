from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct
import hashlib

@app.route("/login", methods=["get", "post"])
def login():
    con = get_db_connection()

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")): 
            return redirect(url_for("profile"), code = 301)
        else:
            session.clear()
            return render_template("login.html")

    #Если осуществляется попытка входа, проверить пару ник/пароль:
    if (request.values.get("nickname") and request.values.get("password")):
        password_hash = hashlib.md5(request.values.get("password").encode("utf-8")).hexdigest()
        if is_nickname_password_pair_correct(con, request.values.get("nickname"), password_hash):
            session["nickname"] = request.values.get("nickname")
            session["password_hash"] = password_hash
            return redirect(url_for("profile"), code = 301)
        else:
            session.clear()
            return render_template("login.html", error_message = "Неправильная пара логин/пароль.")
    else:
        return render_template("login.html")
