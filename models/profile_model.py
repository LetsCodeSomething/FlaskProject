import sqlite3
import pandas

def get_user_posts(con, user_id):
    return pandas.read_sql('''select * from Post where user_id = ?''', params=(user_id,), con=con)

def get_user_images(con, user_id):
    return pandas.read_sql('''select * from Image where user_id = ?''', params=(user_id,), con=con)

def get_user_posts(con, user_id):
    return pandas.read_sql('''select Post.post_id, Post.post_title, Post.post_creation_date,
                                     Post.post_last_update_date, Post.user_id, user_role from Post
                              inner join User u on u.user_id = Post.user_id and u.user_id = ?''', con=con, params=(user_id,))