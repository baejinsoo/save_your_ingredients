import os
import json
import sqlite3


path_dir = './recipes_file'
file_lists = os.listdir(path_dir)

# connect sqlite
conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()
print(conn, cur)

for file in file_lists[10:]:
    file = os.path.abspath('./recipes_file/'+file)
    json_data = open(file, encoding='UTF-8').read()
    json_obj = json.loads(json_data)
    reci_id = json_obj.get("id")
    ingredient_ids = str(json_obj.get("ingredient_ids"))
    ingredient_ids = ingredient_ids.replace('[', '').replace(']', '')
    query = "INSERT INTO recipe_recipe (reci_id,ingredient_ids) VALUES (?,?)"
    cur.execute(query, (reci_id, ingredient_ids))
    # print(ingredient_ids)
    conn.commit()

conn.close()
