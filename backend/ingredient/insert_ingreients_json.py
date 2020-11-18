import os
import json
import sqlite3

file = os.path.abspath('./ingredients/ingredient.json')
json_data = open(file, encoding='UTF-8').read()
json_obj = json.loads(json_data)

# connect sqlite
conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

for data in json_obj:
    data_id = data.get("id")
    data_name = str(data.get("name"))
    data_info = str(data.get("info"))
    data_info = data_info.replace('[', '').replace(']', '')
    data_trim = str(data.get("trim"))
    data_trim = data_trim.replace('[', '').replace(']', '')
    query = "INSERT INTO ingredient_ingredient (id,name,info,trim) VALUES (?,?,?,?)"
    cur.execute(query, (data_id, data_name, data_info, data_trim))
    conn.commit()

conn.close()
