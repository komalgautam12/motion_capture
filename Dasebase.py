from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime

Base =declarative_base()

class Capture(Base):
    __tablename__= 'capture'
    id=Column (Integer,primary_key=True)
    filename=Column (String(50))
    date=Column(DateTime,default=datetime.now)
def __str__(self):
    return self.filename
engine= create_engine("sqlite:///Animation.sqlite",echo=True)


Base.metadata.create_all(engine)