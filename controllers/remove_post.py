from app import app
from flask import request, session, redirect, url_for
from utils import get_db_connection, is_nickname_password_pair_correct, get_user_id, get_user_role
from models.remove_post_model import remove_user_post, user_owns_post

@app.route("/remove_post", methods=["get", "post"])
def remove_post():
    con = get_db_connection()

    if (session.get("nickname") and session.get("password_hash") and
        is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash"))):
        
        user_id = get_user_id(con, request.values.get("nickname"))
        
        if (request.values.get("post_id") and 
            request.values.get("nickname") == session.get("nickname") and
            request.values.get("password_hash") == session.get("password_hash") and
            (user_owns_post(con, request.values.get("post_id"), user_id) or get_user_role(con, user_id))):
                
            remove_user_post(con, request.values.get("post_id"))
            return redirect(url_for("posts"), code=301)
    
    return redirect(url_for("posts"), code=301)