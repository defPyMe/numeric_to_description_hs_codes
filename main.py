import re
import pandas as pd
import sqlite3
from tkinter import *
from tkinter import messagebox
import os, sys

#should get thevalues in the list already created and print them before the results 
#is having more values good? because i cannot have det them by index in a list ??

#creating the interface
root=Tk()
input_box=Text(padx=15)
output_box=Text(padx=15)


root.geometry("400x400")
#initialize the list here

#choosing tje right db
#we can use a list of lists to process this and creeate lists dinamically 

def creating_all_the_dbs_lists():
        global zip_dict
        global dbs
        choice = [ "zero", "one",  "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        dbs = [[] for i in range(10)]
        count = -1
        for i in choice:
                # we index the values in the lists of lists to get what we need
                with sqlite3.connect("C:\\Users\\cavazzinil\\OneDrive - YOOX NET-A-PORTER GROUP\\Desktop\\ff\\hs_codes\\hs_codes.db") as conn:
                        command = ("SELECT codes, description FROM " + i ) #LIKE 'i%'
                        result = conn.execute(command)
                        list_of_results = result.fetchall()
                        zip_dict = (dict(list_of_results))
                count = count + 1
                dbs[count].append(zip_dict)
                

creating_all_the_dbs_lists()


def checking_for_input():
        global results
        global codes 
        codes = []
        results = []
        #getting the inputs 
        #output_box.delete(0, END)
        print("entering the function")
        h=input_box.get("1.0", "end").strip().split()
        no_dupl = list(dict.fromkeys(h))
        for i in no_dupl:
                checking_list_inputs(i)
        for i in range(len(results)):
                output_box.insert("end", codes[i] + "    " + results[i] + '\n')



def clean_the_input(input_word):
        separators = ["-",",", "/", ".", "*", "   ", " ", " m", "m" ,"a", "t", "c", "h", "'", "]", ">", "=", ")"]
        #turning it to string
        new_word = "".join([i for i in input_word if i not in separators])
        return new_word

def calculating_x(base, n):
        global x
        #need to work on the  algorithm here to reload onece it has been checked 
        x = re.search(fr"{base}", n)
        if x!=None:
                return base, n


def checking_list_inputs(word):
        global chosen_list_in_dict
        try:
                cleaned_word =  clean_the_input(word)
                if str.isdigit(cleaned_word[:1]):
                        start_inp = int(cleaned_word[:1])
                        chosen_list = dbs[start_inp]
                        chosen_list_in_dict = {}
                #could have here a mechanisn that checks if the word contains only numbers
                #if not i put it into the output window
                        for i in chosen_list:
                                chosen_list_in_dict.update(i)
                        #needs to be a while loop that strips the values as we go until something is found
                        first_iteration = [calculating_x(cleaned_word, i) for i in chosen_list_in_dict]
                        result_first_iteration = [i for i in first_iteration if i!=None]
                        if len(result_first_iteration)==0:
                                second_iteration = [calculating_x(cleaned_word[:-2], i) for i in chosen_list_in_dict]
                                result_first_iteration = [i for i in second_iteration if i!=None]
                                #(str(result_second_iteration).split(","))[2]
                                #need to index here !!!!! in case it is not found at the first iteration 
                        tupling = tuple(str(result_first_iteration).split(","))
                        output_of_cleaning_tuple = (clean_the_input(tupling[1]))
                
                        
                        results.append(chosen_list_in_dict[output_of_cleaning_tuple])
                        codes.append(output_of_cleaning_tuple)



                        
                        #results.append(" WARNING, NOT FOUND AS A VALID HS CODE")
                        #codes.append(cleaned_word)
                        #print here as both loops have been checked, need to change n here
                        #
                                
                else:
                        results.append(" WARNING, NOT A VALID NUMERIC HS CODE")
                        codes.append(cleaned_word)

        except Exception as e :
                messagebox.showinfo(message='An error has occurred ')
                print(e)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

#tryng to call the function here to see if it works
button_check=Button(text="see variable", command=checking_for_input,padx=15 )
input_box.grid(row=0, column=0)
output_box.grid(row=0, column=1)
button_check.grid(row=1, column=1)


root.mainloop()
