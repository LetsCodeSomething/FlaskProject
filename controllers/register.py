from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, user_exists
from models.register_model import add_user
import hashlib
import string

def is_nickname_valid(nickname):
    if len(nickname) < 1 or len(nickname) > 32:
        return False

    allowed_symbols = string.ascii_letters + string.digits + "_"
    print(allowed_symbols)
    for i in range(len(nickname)):
        if allowed_symbols.find(nickname[i]) == -1:
            return False
    return True

@app.route("/register", methods=["get", "post"])
def register():
    con = get_db_connection()

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")): 
            return redirect(url_for("profile"), code = 301)
        else:
            session.clear()
            return render_template("register.html")

    #Если осуществляется попытка регистрации, проверить, есть ли такой аккаунт в базе:
    if (request.values.get("nickname") and request.values.get("password")):
        nickname = request.values.get("nickname")
        password = request.values.get("password")

        if user_exists(con, nickname):
            return render_template("register.html", error_message = "Никнейм занят, попробуйте выбрать другой.")
        else:
            if is_nickname_valid(nickname):
                add_user(con, nickname, password)
                session["nickname"] = nickname
                session["password_hash"] = hashlib.md5(password.encode("utf-8")).hexdigest()
                return redirect(url_for("profile"), code = 301)
            return render_template("register.html", error_message = "Никнейм может состоять из букв английского алфавита, цифр и \"_\" и должен быть не длиннее 32 символов.")
    else:
        return render_template("register.html")
