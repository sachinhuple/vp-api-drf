# create .sql file from json

import pandas as pd
import json
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()


def load_json():
    with open('playlist.json', 'r') as file:
        data = json.load(file)
    columns = list(data.keys())
    columns.append('star_rating')
    df = pd.DataFrame(data, columns=columns)
    # df.to_csv('playlist.csv', index=False)
    df.to_sql('song', conn, if_exists='replace')


load_json()
