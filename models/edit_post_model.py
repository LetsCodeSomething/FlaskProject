import pandas

def user_owns_post(con, user_id, post_id):
    return pandas.read_sql('''select * from Post where user_id = ? and post_id = ?''', params=(user_id, post_id) ,con=con).shape[0] > 0

def get_post(con, post_id):
    return pandas.read_sql('''select * from Post where post_id = ?''', params=(post_id,), con=con)

def update_post(con, post_id, post_title, post_text):    
    if len(post_title) > 32 or len(post_text) > 512:
        return
    con.execute('''update Post set post_title = ?, post_text = ?, post_last_update_date = datetime("now") 
                   where post_id = ?''', (post_title, post_text, post_id))
    con.commit()