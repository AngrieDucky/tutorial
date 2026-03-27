import re
from quart_wtf import QuartForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError
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
    
    
class MetroForm(QuartForm):
    metro_station = StringField(label="Станция Метро", validators=[DataRequired("Станция метро не может быть пустой"), 
                                                                   Length(3, 30, "Название станции метро не может быть длиннее 30 символов")])
    fio = StringField(label="ФИО Заказчика", validators=[DataRequired("ФИО заполнять обязательно"), 
                                                                   Length(3, 100, "Слишком длинное имя. Используйте инициалы.")])
    
class IsAlNum():
    def __call__(self, form, field: str):
        if not field.isalnum():
            raise ValidationError("Invalid input syntax")    

    
class FormReg(QuartForm):
    login = StringField(label="Логин",
                        validators=[
                            Length(min=6),
                            IsAlNum()
                        ])
    password = PasswordField(label="Пароль",
                           validators=[
                            Length(min=6)
                            ])
    full_name = StringField(label="Полное ФИО")
    phone = StringField()
    email = EmailField(label="email", validators=[Email()])
    

        
