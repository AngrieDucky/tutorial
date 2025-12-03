import datetime
from functools import wraps
import os
from quart import abort, render_template, request, jsonify, send_from_directory
import asyncio
import sqlalchemy
from sqlalchemy.orm import Session

from quart_ import app
from quart_.models import UserTable
from quart_.forms import RegForm
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
async def main_page():
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
    return await render_template("index.html", form=RegForm())

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
    
# ============================= Error Handlers ===========================

@app.errorhandler(404)
async def page_not_found(error):
    print(error)
    return await render_template("index.html", form=RegForm())

@app.errorhandler(500)
async def internal_error(error):
    return jsonify({"message": "This is an error", "status_code": 500})
