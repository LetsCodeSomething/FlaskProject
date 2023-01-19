import pandas

def image_exists(con, image_id):
    return pandas.read_sql('''select * from Image where image_id = ?''', params=(int(image_id),), con=con).shape[0] > 0

def add_image(con, user_id, base64, origin, formula, palette, dx, dy, cx, cy, scale, bailout, n, width, height):
    max_image_id = 0
    df = pandas.read_sql('''select max(image_id) + 1 as image_id from Image''', con)
    if df.loc[0, "image_id"]:
        max_image_id = int(df.loc[0, "image_id"])
    
    if formula == "Множество Мандельброта":
        formula = 0
    else:
        formula = 1
    
    if palette == "Чёрно-белая":
        palette = 0
    elif palette == "Градиентная":
        palette = 1
    else:
        palette = 2

    con.execute('''insert into Image(image_id, user_id, image_base64, image_origin_post_id, image_formula,
                                     image_palette, image_dx, image_dy, image_cx, image_cy, image_scale,
                                     image_bailout, image_n, image_width, image_height)
                   values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (max_image_id, user_id, base64, origin, formula,
                    palette, dx, dy, cx, cy, scale, bailout, n, width, height))
    con.commit()

def user_owns_image(con, image_id, user_id):
    return pandas.read_sql('''select * from Image where image_id = ?''', con=con, params=(image_id,)).loc[0, "user_id"] == user_id

def update_image(con, image_id, user_id, base64, origin, formula, palette, dx, dy, cx, cy, scale, bailout, n, width, height):
    if formula == "Множество Мандельброта":
        formula = 0
    else:
        formula = 1
    
    if palette == "Чёрно-белая":
        palette = 0
    elif palette == "Градиентная":
        palette = 1
    else:
        palette = 2

    con.execute('''update Image set user_id = ?, image_base64 = ?, image_origin_post_id = ?, image_formula = ?,
                                     image_palette = ?, image_dx = ?, image_dy= ?, image_cx=?, image_cy=?, image_scale=?,
                                     image_bailout = ?, image_n = ?, image_width = ?, image_height = ? where image_id = ?''', 
                   (user_id, base64, origin, formula,
                    palette, dx, dy, cx, cy, scale, bailout, n, width, height, image_id))
    con.commit()