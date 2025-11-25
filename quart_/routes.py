from functools import wraps
from quart import Quart, abort, render_template, request
import asyncio
import re
from quart_wtf import QuartForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, Length
from wtforms.widgets import PasswordInput

class SomeForm(QuartForm):
    email = StringField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )

class RegForm(QuartForm):
    username = StringField(label="Username", 
                           validators=[DataRequired("Username is required"), 
                                        Length(max=128, min=4, message="Please make sure your username is  more than 4 and less than 128 bytes")])
    password = PasswordField("Very Secret Password", 
                             validators=[DataRequired("Password is required"), 
                                        Regexp(regex=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[=#_$!?])[a-zA-Z\d=#_$!?]$"), message="Passwod should be ..."), 
                                        Length(3, 256, "password shoulf be at least 3 and at worst 256 bytes")])
    

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
        form_data["username"]
    ctx: dict = {"form": RegForm()}
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
    app.run()