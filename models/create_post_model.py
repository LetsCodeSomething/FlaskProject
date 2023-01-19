import pandas

def add_post(con, post_title, post_text, image_id, user_id):
    max_post_id = 0
    df = pandas.read_sql('''select max(post_id) + 1 as post_id from Post''', con)
    if df.loc[0, "post_id"]:
        max_post_id = int(df.loc[0, "post_id"])
    
    if len(post_title) > 32 or len(post_text) > 512:
        return

    con.execute('''insert into Post(post_id, post_title, post_text, post_creation_date, post_last_update_date,
                                    image_id, user_id)
                   values(?, ?, ?, datetime("now"), datetime("now"), ?, ?)''', (max_post_id, post_title, post_text, image_id, user_id))
    con.commit()