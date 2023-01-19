from app import app
from flask import render_template, session, request, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, post_exists, get_image_base64, get_post_ex, get_user_id, get_user_role

@app.route("/read_post", methods=["get"])
def read_post():
    con = get_db_connection()
    
    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash") and
        is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")) and
        request.values.get("post_id") and post_exists(con, request.values.get("post_id"))):
        df = get_post_ex(con, request.values.get("post_id"))
        user_id = get_user_id(con, session.get("nickname"))
        user_role = get_user_role(con, int(user_id))
        return render_template("read_post.html",
                               post = df,
                               nickname = session.get("nickname"),
                               password_hash = session.get("password_hash"),
                               user_id = user_id,
                               user_role = user_role)

    return redirect(url_for("posts"), code=301)