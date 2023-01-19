from app import app
from flask import request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id
from models.save_image_model import image_exists, add_image, user_owns_image, update_image

@app.route("/save_image", methods=["get", "post"])
def save_image():
    con = get_db_connection()
    
    #Изображение сохраняется, только если есть активная сессия, пользователь есть в базе,
    #в параметрах запроса есть флаг об удалении и ник с хешем, совпадающие с теми, что есть в сессии:
    if (session.get("nickname") and session.get("password_hash")):
        if (is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash"))
            and session.get("nickname") == request.values.get("nickname")
            and session.get("password_hash") == request.values.get("password_hash") and
            request.values.get("base64") and
            request.values.get("formula") and request.values.get("palette") and
            request.values.get("dx") and request.values.get("dy") and
            request.values.get("cx") and request.values.get("cy") and
            request.values.get("scale") and request.values.get("bailout") and
            request.values.get("n") and request.values.get("width") and
            request.values.get("height")): 
            
            #Если осуществляется попытка обновить изображение
            if request.values.get("image_id") and image_exists(con, request.values.get("image_id")):
                if user_owns_image(con, request.values.get("image_id"), get_user_id(con, session.get("nickname"))):
                    update_image(con, 
                              request.values.get("image_id"),
                              get_user_id(con, session.get("nickname")),
                              request.values.get("base64"),
                              request.values.get("origin"),
                              request.values.get("formula"),
                              request.values.get("palette"),
                              request.values.get("dx"),
                              request.values.get("dy"),
                              request.values.get("cx"),
                              request.values.get("cy"),
                              request.values.get("scale"),
                              request.values.get("bailout"),
                              request.values.get("n"),
                              request.values.get("width"),
                              request.values.get("height"))
            else:
                if request.values.get("origin"):
                    add_image(con, get_user_id(con, session.get("nickname")),
                              request.values.get("base64"),
                              request.values.get("origin"),
                              request.values.get("formula"),
                              request.values.get("palette"),
                              request.values.get("dx"),
                              request.values.get("dy"),
                              request.values.get("cx"),
                              request.values.get("cy"),
                              request.values.get("scale"),
                              request.values.get("bailout"),
                              request.values.get("n"),
                              request.values.get("width"),
                              request.values.get("height"))
                else:
                    add_image(con, get_user_id(con, session.get("nickname")),
                              request.values.get("base64"),
                              -1,
                              request.values.get("formula"),
                              request.values.get("palette"),
                              request.values.get("dx"),
                              request.values.get("dy"),
                              request.values.get("cx"),
                              request.values.get("cy"),
                              request.values.get("scale"),
                              request.values.get("bailout"),
                              request.values.get("n"),
                              request.values.get("width"),
                              request.values.get("height"))
            return redirect(url_for("profile"), code=301)

    return redirect(url_for("index"), code=301)
