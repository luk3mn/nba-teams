from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Table(Base):
    __tablename__ = 'tb_nba'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    conference = Column(String)
    city = Column(String)

    def start():
        db_string = '' # conection database
        engine = create_engine(db_string) # define the engine
        Session = sessionmaker(bind=engine) # create the session
        session = Session()
        Base.metadata.create_all(engine)
        print('\nTable created on database')
        return session, engine