def remove_user(con, user_id):
    con.execute("delete from User where user_id = ?", (user_id,))
    con.execute("delete from Post where user_id = ?", (user_id,))
    con.execute("delete from Image where user_id = ?", (user_id,))
    con.commit()