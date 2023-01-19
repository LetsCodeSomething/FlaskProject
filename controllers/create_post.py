from app import app
from flask import render_template, session, request, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id, get_image_base64, image_exists
from models.create_post_model import add_post

@app.route("/create_post", methods=["get", "post"])
def create_post():
    con = get_db_connection()

    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    if (session.get("nickname") and session.get("password_hash") and
        is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")) and
        request.values.get("image_id") and image_exists(con, request.values.get("image_id"))):
        if (request.values.get("post_title") and request.values.get("post_text")):
            add_post(con, request.values.get("post_title"), request.values.get("post_text"),
                     request.values.get("image_id"), get_user_id(con, session.get("nickname")))
            return redirect(url_for("posts"), code=301)
        return render_template("create_post.html",
                               nickname = session.get("nickname"),
                               image_id = request.values.get("image_id"),
                               image_base64 = get_image_base64(con, request.values.get("image_id")))

    return redirect(url_for("posts"), code=301)