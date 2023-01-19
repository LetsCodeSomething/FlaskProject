import pandas

def remove_user_image(con, image_id):
    con.execute("delete from Image where image_id = ?", (image_id,))
    #con.execute("delete from Post where image_id = ?", (image_id,))
    con.commit()

def user_owns_image(con, image_id, user_id):
    return pandas.read_sql('''select * from Image where image_id = ?''', con=con, params=(image_id,)).loc[0, "user_id"] == user_id