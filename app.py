# Reference: https://www.dataside.com.br/post/saiba-como-consumir-dados-de-um-json-direto-de-uma-api
# name, abbreviation, conference and city

import pandas as pd
import json

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