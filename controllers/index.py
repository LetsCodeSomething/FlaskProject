from app import app
from flask import render_template, request, session
from utils import get_db_connection, is_nickname_password_pair_correct

@app.route('/', methods=['get'])
def index():
    con = get_db_connection()
    
    #Если в атрибутах сессии уже есть ник и хеш, пытаться найти пользователя в базе:
    nickname = None
    if (session.get("nickname") and session.get("password_hash")):
        if is_nickname_password_pair_correct(con, session.get("nickname"), session.get("password_hash")): 
            nickname = session.get("nickname")
        else:
            session.clear()

    if (request.values.get('formula') and
        request.values.get('palette') and
        request.values.get('dx') and
        request.values.get('dy') and
        request.values.get('scale') and
        request.values.get('bailout') and
        request.values.get('n') and
        request.values.get('width') and
        request.values.get('height')):
        
        html = render_template(
            'index.html',
            formulas = ["Множество Мандельброта", "Множество Жюлиа"],
            formula = request.values.get('formula'),
            palettes = ["Чёрно-белая", "Градиентная", "Оттенки синего"],
            palette =request.values.get('palette'),
            dx = request.values.get('dx'),
            dy = request.values.get('dy'),
            cx = request.values.get('cx'),
            cy = request.values.get('cy'),
            scale = request.values.get('scale'),
            bailout = request.values.get('bailout'),
            n = request.values.get('n'),
            width = request.values.get('width'),
            height = request.values.get('height'),
            nickname = nickname,
            password_hash = session.get("password_hash"),
            origin = request.values.get('origin'),
            image_id = request.values.get('image_id'),
            len = len
            )
    else:
        html = render_template(
            'index.html',
            formulas = ["Множество Мандельброта", "Множество Жюлиа"],
            formula = 0,
            palettes = ["Чёрно-белая", "Градиентная", "Оттенки синего"],
            palette = 0,
            dx = 0,
            dy = 0,
            scale = 0.006,
            bailout = 2,
            n = 50,
            width = 500,
            height = 250,
            nickname = nickname,
            password_hash = session.get("password_hash"),
            len = len
            )

    return html