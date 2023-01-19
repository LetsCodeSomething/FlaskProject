from app import app
from flask import render_template, session, request, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id
from models.profile_model import get_user_posts, get_user_images

@app.route("/profile", methods=["get"])
def profile():
    con = get_db_connection()

    if request.values.get("exit"):
        session.clear()
        return redirect(url_for("index"), code=301)

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")):
            #Если пользователь хочет выйти из аккаунта:
            if request.values.get("exit"):
                session.clear()
                return redirect(url_for("index"), code=301)

            return render_template("profile.html", 
                                   nickname = session.get("nickname"),
                                   password_hash = session.get("password_hash"),
                                   user_posts = get_user_posts(con, get_user_id(con, session.get("nickname"))),
                                   user_images = get_user_images(con, get_user_id(con, session.get("nickname"))),
                                   len = len)

    session.clear()
    return redirect(url_for("index"), code=301)