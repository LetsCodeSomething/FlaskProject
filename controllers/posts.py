from app import app
from flask import render_template, session
from utils import get_db_connection, is_nickname_password_pair_correct, get_posts_ex

@app.route("/posts", methods=["get"])
def posts():
    con = get_db_connection()

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")): 
            return render_template("posts.html", 
                                   nickname = session.get("nickname"),
                                   posts = get_posts_ex(con),
                                   len = len)

    return render_template("posts.html", 
                           posts = get_posts_ex(con), 
                           len = len)