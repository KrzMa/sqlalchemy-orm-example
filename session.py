from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'mysql+pymysql://root:Luffy123@localhost:3306/blog'
)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

