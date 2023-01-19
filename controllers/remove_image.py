from app import app
from flask import request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id
from models.remove_image_model import remove_user_image, user_owns_image

@app.route("/remove_image", methods=["get", "post"])
def remove_image():
    con = get_db_connection()

    #Изображение удаляется, только если есть активная сессия, пользователь есть в базе,
    #в параметрах запроса есть флаг об удалении и ник с хешем, совпадающие с теми, что есть в сессии:
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")):
            if (request.values.get("image_id") and 
                request.values.get("nickname") == session.get("nickname") and
                request.values.get("password_hash") == session.get("password_hash") and
                user_owns_image(con, request.values.get("image_id"), get_user_id(con, request.values.get("nickname")))):
                remove_user_image(con, request.values.get("image_id"))
                return redirect(url_for("profile"), code=301)
    
    return redirect(url_for("profile"), code=301)