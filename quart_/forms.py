import re
from quart_wtf import QuartForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, Length

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
                                        Length(max=128, min=4, 
                                               message="Please make sure your username is  more than 4 and less than 128 bytes")])
    password = PasswordField("Very Secret Password", 
                             validators=[DataRequired("Password is required"), 
                                        Regexp(regex=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[=#_$!?])[a-zA-Z\d=#_$!?]$"), 
                                               message="Passwod should be ..."), 
                                        Length(3, 256, "password should be at least 3 and at worst 256 bytes")])