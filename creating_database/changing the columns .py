import pandas as pd

df = pd.read_excel("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\CN_2022_ALL_LANGUAGES.xlsx")

list_column = list(df["description"])

for i in list_column :
	if i == "Other":
		#getting the index
		index = list_column.index(i)
		#now i replace the value in the index with the values in other preceding indexes (2 back)
		comment = list_column[index] + "  " +  list_column[index -1] + "   " + list_column[index -2]
		list_column[index] = comment
with open ("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\new_column.txt", "w", encoding="utf-8") as txt:
        #getting problems with the / character, removed and now ok 
		#printing on different lines 
        txt.write('\n'.join(list_column))
