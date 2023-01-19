import sqlite3
import pandas

def get_db_connection():
    return sqlite3.connect('db.sqlite')

def is_nickname_password_pair_correct(con, nickname, password_hash):
    df = pandas.read_sql('''select user_id from User 
                            where user_nickname = ? and 
                            user_password_hash = ?''', params=(nickname, password_hash,),con=con)
    if df.shape[0] > 0:
        return True
    return False

def user_exists(con, nickname):
    if pandas.read_sql('''select user_id from User where user_nickname = ?''', params=(nickname,),con=con).shape[0] > 0:
        return True
    return False

def image_exists(con, image_id):
    if pandas.read_sql('''select image_id from Image where image_id = ?''', params=(image_id,),con=con).shape[0] > 0:
        return True
    return False

def post_exists(con, post_id):
    if pandas.read_sql('''select post_id from Post where post_id = ?''', params=(post_id,),con=con).shape[0] > 0:
        return True
    return False

def get_user_id(con, nickname):
    user_id = pandas.read_sql('''select user_id from User where user_nickname = ?''', params=(nickname,), con=con).loc[0, "user_id"]
    user_id = int(user_id)
    return user_id

def get_user_role(con, user_id):
    return pandas.read_sql('''select user_role from User where user_id = ?''', params=(user_id,), con=con).loc[0, "user_role"]

def get_image_base64(con, image_id):
    return pandas.read_sql('''select image_base64 from Image where image_id = ?''', params=(image_id,), con=con).loc[0, "image_base64"]

def get_posts_ex(con):
    df = pandas.read_sql('''select Post.post_id, Post.post_title, Post.post_text, Post.post_creation_date,
                                   Post.post_last_update_date, Post.image_id, Post.user_id, user_role, user_nickname from Post
                            inner join User u on u.user_id = Post.user_id''', con)
    return df

def get_post_ex(con, post_id):
    df = pandas.read_sql('''select Post.post_id, Post.post_title, Post.post_text, Post.post_creation_date,
                                   Post.post_last_update_date, Post.image_id, Post.user_id, user_role, user_nickname, 
                                   image_base64, image_origin_post_id, image_formula,
                                   image_palette, image_dx, image_dy, image_cx,
                                   image_cy, image_scale, image_bailout,
                                   image_n, image_width, image_height
                                   from Post
                            inner join User u on u.user_id = Post.user_id
                            inner join Image i on i.image_id = Post.image_id 
                            where Post.post_id = ?''', params=(post_id,),con=con)
    return df