from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

engine = create_engine('mysql://root:1KW48OdR2QR7W6VELuta@containers-us-west-72.railway.app:8038/railway')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()