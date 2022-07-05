import db

from sqlalchemy import Column, Integer, String, Float, DateTime


class Partidos(db.Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    local = Column(String)
    visitante = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow())
    last_update = Column(DateTime, default=datetime.utcnow())
    score = Column(String, default='0-0')
    Status = Column(String)

    def __init__(self):
        pass

class Test(db.Base):
    __tablename__ = 'testing'

    id = Column(Integer, primary_key=True)
    test = Column(String)
    value = Column(Integer)

    def __init__(self, value, test='prueba'):
        self.test = test
        self.value = value