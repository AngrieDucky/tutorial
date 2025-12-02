from sqlalchemy import String, Time, Boolean
import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserTable(Base):
    __tablename__ = "auth_user"

    _id: Mapped[int] = mapped_column("id", primary_key=True, index=True, autoincrement=True)
    password: Mapped[str] = mapped_column(String(128))
    last_login: Mapped[str] = mapped_column(Time(True))
    is_superuser: Mapped[bool] = mapped_column(Boolean())
    username: Mapped[str] = mapped_column("username", String(150))
    first_name: Mapped[str] = mapped_column(String(150))
    last_name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(254))
    is_staff: Mapped[bool] = mapped_column(Boolean())
    is_active: Mapped[bool] = mapped_column(Boolean())
    date_joined: Mapped[str] = mapped_column(Time(True))
    
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