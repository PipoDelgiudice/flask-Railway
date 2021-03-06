import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

base_address = os.getenv("MySQL", default='mysql+pymysql://root:hNwj28bfJwb1kDgFqyy9@containers-us-west-71.railway.app:7865/railway')
engine = create_engine(base_address)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()