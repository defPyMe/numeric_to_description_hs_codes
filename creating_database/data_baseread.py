import sqlite3
import pandas as pd
import os.path

#BASE_DIR = os.path.dirname(os.path.abspath("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\"))
#db_path = os.path.join(BASE_DIR, "hs_codes.db")

df = pd.read_excel("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\CN_2022_ALL_LANGUAGES.xlsx")

index = list(df['index'])
column = list(df['taric_code'])
column_string = list(map(str, column))
#CONVERTING THe integers to lists 
column_description = list(df['description'])
column_string_descr = list(map(str, column_description))

for i in range(14999):
    
    y = str(column_string[i])
    z = str(column_string_descr[i])
    print(i)
    with sqlite3.connect("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\hs_codes.db") as conn:
        #"INSERT INTO codes_table(index, codes, description) VALUES(?,?,?)", (x, y, z)
        command = "INSERT INTO creation(codes, description) VALUES(?,?)"
        try:
            conn.execute(command, (y,z))
        except Exception as e:
            print(e)
        conn.commit()



