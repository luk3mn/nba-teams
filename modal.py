from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Table define
class Franchise(Base):
    __tablename__ = 'tb_nba'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    conference = Column(String)
    city = Column(String)
    # division = Column(String)

    def start():
        # 'postgresql://username:password@endpoint/database'
        db_string = 'postgresql://postgres:Teste321@server01.crlnbuyeleti.us-east-1.rds.amazonaws.com/teste' # conection database
        engine = create_engine(db_string) # define the engine
        Session = sessionmaker(bind=engine) # create the session
        session = Session()
        Base.metadata.create_all(engine)
        print('\nTable created on database')
        return session, engine