import db

from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime
from dataclasses import dataclass


@dataclass
class Partidos(db.Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    local = Column(String(40))
    visitante = Column(String(40))
    fecha = Column(DateTime, default=datetime.datetime.utcnow())
    last_update = Column(DateTime, default=datetime.datetime.utcnow())
    score = Column(String(40), default='0-0')
    Status = Column(String(40))

    def __init__(self, id, local=None, visitante=None, fecha=None, score=None, Status=None):
        self.id = id
        self.local = local
        self.visitante = visitante
        self.fecha = fecha
        self.score = score
        self.Status = Status
        self.last_update = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

@dataclass
class Match:
    id = None
    local = None
    visitante = None
    fecha = None
    last_update = None
    score = None
    Status = None


@dataclass
class Test(db.Base):
    __tablename__ = 'testing'

    id = Column(Integer, primary_key=True)
    test = Column(String(40))
    value = Column(Integer)

    def __init__(self, value=None, test='prueba'):
        self.test = test
        self.value = value