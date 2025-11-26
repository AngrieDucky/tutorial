import datetime
from functools import wraps
from quart import Quart, abort, render_template, request
import asyncio
import re
from quart_wtf import QuartForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, Length
from wtforms.widgets import PasswordInput
import sqlalchemy
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

engine: sqlalchemy.Engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/postgres", connect_args={'options': '-csearch_path={}'.format("public")})

class Base(DeclarativeBase):
    pass

class UserTable(Base):
    __tablename__ = "auth_user"

    _id: Mapped[int] = mapped_column("id", primary_key=True, index=True, autoincrement=True)
    password: Mapped[str] = mapped_column(sqlalchemy.String(128))
    last_login: Mapped[str] = mapped_column(sqlalchemy.Time(True))
    is_superuser: Mapped[bool] = mapped_column(sqlalchemy.Boolean())
    username: Mapped[str] = mapped_column("username", sqlalchemy.String(150))
    first_name: Mapped[str] = mapped_column(sqlalchemy.String(150))
    last_name: Mapped[str] = mapped_column(sqlalchemy.String(150))
    email: Mapped[str] = mapped_column(sqlalchemy.String(254))
    is_staff: Mapped[bool] = mapped_column(sqlalchemy.Boolean())
    is_active: Mapped[bool] = mapped_column(sqlalchemy.Boolean())
    date_joined: Mapped[str] = mapped_column(sqlalchemy.Time(True))
    
    def __init__(self, password: str, username: str):
        self.username = username
        self.password = password
        self.last_login = datetime.datetime.now()
        self.is_active = True
        self.is_staff = False
        self.is_superuser = False
        self.email = ""
        self.last_name = ""
        self.first_name = ""
        self.date_joined = datetime.datetime.now()
        
    def __repr__(self):
        return f"{self.username} from table {self.__tablename__} joined at {self.date_joined}"
        

class SomeForm(QuartForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def update_password(self, new_password):
        self.password = new_password
        

class RegForm(QuartForm):
    username = StringField(label="Username", 
                           validators=[DataRequired("Username is required"), 
                                        Length(max=128, min=4, 
                                               message="Please make sure your username is  more than 4 and less than 128 bytes")])
    password = PasswordField("Very Secret Password", 
                             validators=[DataRequired("Password is required"), 
                                        Regexp(regex=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[=#_$!?])[a-zA-Z\d=#_$!?]$"), 
                                               message="Passwod should be ..."), 
                                        Length(3, 256, "password should be at least 3 and at worst 256 bytes")])
    

app = Quart(__name__)
app.secret_key = "Very_secret_much_wow"

def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if request.authentication == (...):
            return await func(*args, **kwargs)
        else:
            abort(401)
    return wrapper

@app.get('/')
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

if __name__ == "__main__":
    # C:\Users\minak\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts
    app.run()