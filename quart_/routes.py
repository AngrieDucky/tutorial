import datetime
from functools import wraps
import os
from quart import abort, render_template, request, jsonify, send_from_directory, redirect, url_for
import asyncio
import random
import sqlalchemy
from sqlalchemy.orm import Session

from quart_ import app
from quart_.models import UserTable
from quart_.forms import RegForm, MetroForm
from quart_.user import User
from quart_ import CONN_STRING

engine: sqlalchemy.Engine = sqlalchemy.create_engine(CONN_STRING, connect_args={'options': '-csearch_path={}'.format("public")})  

def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if request.authentication == (...):
            return await func(*args, **kwargs)
        else:
            abort(401)
    return wrapper

@app.get('/imdx')
@app.route('/', methods=["GET", "POST"])
async def main():
    ctx: dict = {"title": "Главная"}
    metroform = MetroForm()
    
    if request.method == "POST":
        unknown = 'Не указано'
        form_data = await request.form
        
        if 'review-from' in form_data:
            metro = form_data["order-station"] # если пользователь ничего не написал - ошибка 500
            metro = form_data.get('order-station', 'Не указано') # Если пользователь прислал слишком много
            if ";" in metro:
                return await render_template("index.html", context=ctx)
            who_asked = form_data.get('order-fio', 'Не указано')
                
            result_1 = ["ЗАКАЗ КОНЦЕРТА:", "Станция метро:", "ФИО заказчика:"]
            
            delimiter = "=" * 50
            newline = "\n".join(result_1)
            print(f"{delimiter}\n{newline}\n{delimiter}")
    
    return await render_template("index.html", context=ctx)
    form_data = await request.form
    if form_data:
        print("yay")
        user = User(form_data["username"], form_data["password"])
    ctx: dict = {"form": RegForm()}
    
    olegs: list[UserTable] = []
    # stmt = "SELECT * FROM pg_catalog.pg_tables"
    # with engine.connect() as conn:
    #     res = conn.execute(sqlalchemy.text(stmt))
    #     for row in res:
    #         print(row)
    with Session(engine) as session:
        try:
            
            stmt = sqlalchemy.select(UserTable).filter(UserTable.username == "Oleg")
            # select * from user where name == 'Олег';
            print(stmt)
            _olegs = session.scalars(stmt)
            olegs.extend(_olegs)
        except Exception as e:
            print(e)
    
    print(olegs)
    ctx: dict = {"title": "Главная"}
    return await render_template("index.html", context=ctx)


@app.get('/rand_fact')
async def random_fact():
    x = ["Случайный факт номер 1", "Совершенно неслучайный факт", "Не факт, что это - случайность", "Олег - лучший уличный музыкант"]
    num = random.randint(0,3)
    return jsonify({"message": x[num], "status_code": 200})


def generate_twitter_meta(oleg_site:str=""):
    if not oleg_site:
        oleg_site = "http://oleg-site.ru"
    result = f"""
    <meta name="twitter:title" content="Machine Learning Workshop" />
    <meta name="twitter:description" content="School for machines who can't learn good and want to do other stuff good too" />
    <meta name="twitter:url" content="{oleg_site}" />
    <meta name="twitter:image:src" content="http://oleg-site.ru/static/pictures/Rectangle9.png" />
    <meta name="twitter:image:alt" content="Олег: играет и поёт" />
    <meta name="twitter:creator" content="@0leg" />
    <meta name="twitter:site" content="@0leg" />
    """
    return result

@app.route("/design", methods=["GET", "POST"])
async def design_page():
    return "ok"

# @app.route("/<path:path>")
# async def anyotherpage(path_that_we_have_entered):
#     # await asyncio.sleep(5)
#     print(path_that_we_have_entered)
#     return "throw money directly at your screen"

@login_required
@app.route('/homepage', methods=["POST", "PUT", "DELETE"])
async def homepage():
    return await render_template("index.html")

@app.route("/teapot", methods=["GET"])
async def teapot():
    abort(418)
    
@app.route("/error")
async def this_is_an_error():
    abort(500)
    
def unknown_func():
    pass
    
# ============================= Error Handlers ===========================

@app.errorhandler(404)
async def page_not_found(error):
    print(error)
    return await render_template("index.html", form=RegForm())

@app.errorhandler(500)
async def internal_error(error):
    return jsonify({"message": "This is an error", "status_code": 500})

# quart --debug run --port 8000
