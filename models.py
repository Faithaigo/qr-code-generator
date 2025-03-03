from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str] 
    phone:Mapped[str] 
    email:Mapped[str] 
    address:Mapped[str] 
    company_name:Mapped[str]
    company_tag_line:Mapped[str] 
    company_website:Mapped[str]  