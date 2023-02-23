# Reference: https://www.dataside.com.br/post/saiba-como-consumir-dados-de-um-json-direto-de-uma-api
# name, abbreviation, conference and city

import pandas as pd
import json
from modal import Table
from sqlalchemy.ext.declarative import declarative_base

def load_data(table_name, df, session_db, engine_db):

    try:
        df.to_sql(table_name, engine_db, index=False, if_exists='append') # transform in sql
        print('\nData loaded on database')

    except Exception as err:
        print(f"\nFail to load data on database: {err}")
    
    session_db.commit()
    session_db.close() # shutdown the session
    print("\nClose database successfully")
    return session_db

# reading data in json file
with open('data/teams.json') as json_file:
    data = json.load(json_file)

# creating the lists
name = []
abbreviation = []
conference = []
city = []

# writing data in a new variable
for d in data['data']:
    name.append(d['name'])
    abbreviation.append(d['abbreviation'])
    conference.append(d['conference'])
    city.append(d['city'])

# structure data
nba_dict = {
    "name": name,
    "abbreviation": abbreviation,
    "conference": conference,
    "city": city
}

nba_df = pd.DataFrame(nba_dict, columns=['name','abbrevition','conference','city'])
print(nba_df)

# declarative base
# Base = declarative_base()

# Construct the table
get_session_db, get_engine = Table.start()

# call the function to load data on database
load_data(table_name='tb_nba', df=nba_df, session_db=get_session_db, engine_db=get_engine)