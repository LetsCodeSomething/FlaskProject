import sqlite3
import hashlib
import pandas

def add_user(con, nickname, password):
    password_hash = hashlib.md5(password.encode("utf-8")).hexdigest()
    df = pandas.read_sql('''select max(user_id) + 1 as user_id from User''', con)
    max_user_id = 0
    if df.loc[0, "user_id"]:
        max_user_id = int(df.loc[0, "user_id"])

    con.execute('''insert into User(user_id, user_nickname, user_password_hash, user_registration_datetime, user_role)
                    values (?, ?, ?, datetime("now"), 0)''', (max_user_id, nickname, password_hash,))
    con.commit()
