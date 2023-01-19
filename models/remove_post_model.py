import pandas

def user_owns_post(con, post_id, user_id):
    return pandas.read_sql('''select * from Post where post_id = ? and user_id = ?''', con=con, 
                           params=(post_id,user_id,)).shape[0] > 0

def remove_user_post(con, post_id):
    con.execute('''delete from Post where post_id = ?''', (post_id,))
    con.commit()