import pandas

def get_post(con, post_id):
    return pandas.read_sql('''select * from Post where post_id = ?''', params=(post_id,), con=con)