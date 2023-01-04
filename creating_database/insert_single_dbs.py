import sqlite3
import pandas as pd

#when we have a column that has zeroes in front we wish to keep we can use the converters keyword argument to keep the zero
#can be left there if we are storing strings 
df = pd.read_excel("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\split db\\zero.xlsx", converters={'taric_code': str})


column = list(df['taric_code'])
print(column)
column_string = list(map(str, column))
#CONVERTING THe integers to lists 
column_description = list(df['description'])
column_string_descr = list(map(str, column_description))

for i in range(len(column_string_descr)):
    y = str(column_string[i])
    z = str(column_string_descr[i])
    print(y)
    with sqlite3.connect("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\hs_codes.db") as conn:
        #"INSERT INTO codes_table(index, codes, description) VALUES(?,?,?)", (x, y, z)
        command = "INSERT INTO zero(codes, description) VALUES(?,?)"
        try:
            conn.execute(command, (y,z))
        except Exception as e:
            print(e)
        conn.commit()
