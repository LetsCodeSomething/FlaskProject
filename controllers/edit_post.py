from app import app
from flask import render_template, session, request, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id, get_image_base64, image_exists, get_user_role
from models.edit_post_model import update_post, user_owns_post, get_post
import pandas

@app.route("/edit_post", methods=["get", "post"])
def edit_post():
    con = get_db_connection()

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash") and
        is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")) and
        request.values.get("post_id") and (get_user_role(con, get_user_id(con, session.get("nickname"))) == 1 or user_owns_post(con, get_user_id(con, session.get("nickname")), request.values.get("post_id")))):
        if (request.values.get("post_title") and request.values.get("post_text")):
            update_post(con, request.values.get("post_id"), request.values.get("post_title"), request.values.get("post_text"))
            return redirect(url_for("posts"), code=301)
        df = get_post(con, request.values.get("post_id"))
        return render_template("edit_post.html",
                               post_id = request.values.get("post_id"),
                               post_title = df.loc[0, "post_title"],
                               post_text = df.loc[0, "post_text"],
                               nickname = session.get("nickname"))

    return redirect(url_for("posts"), code=301)