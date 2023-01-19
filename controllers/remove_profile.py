from app import app
from flask import request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id
from models.remove_profile_model import remove_user

@app.route("/remove_profile", methods=["get", "post"])
def remove_profile():
    con = get_db_connection()

    #Профиль удаляется, только если есть активная сессия, пользователь есть в базе,
    #в параметрах запроса есть флаг об удалении и ник с хешем, совпадающие с теми, что есть в сессии:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")):
            if (request.values.get("remove") and 
                request.values.get("nickname") == session.get("nickname") and
                request.values.get("password_hash") == session.get("password_hash")):
                remove_user(con, get_user_id(con, session.get("nickname")))
                session.clear()
                return redirect(url_for("index"), code=301)
    
    return redirect(url_for("profile"), code=301)