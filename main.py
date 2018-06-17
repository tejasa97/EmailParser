#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:36:49 2018

@author: tejas
"""
#Import all necessary modules

from tabulate import tabulate
import sys
import time
from datetime import datetime, date
import csv
import numpy as np
import pandas as pd

#Empty arrays to buffer data from the CSV
temp, row = ([] for i in range(2))
csv_file = sys.argv[1]

def pretty_print_df(df):
    print (tabulate(df, headers='keys', tablefmt='psql'))
  
#Open CSV and dump data into array 'row'
with open(csv_file, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        temp.append(' '.join(row))

for i in range(len(temp) - 1):
    row.append(temp[i+1].split('$'))
    
date, email, u_email, msg = ([] for i in range(4))

key_word = []
for i in range(len(row)):
    try:
        datetime.strptime(row[i][0], "%d/%m/%y")
        date.append(row[i][0])
        email.append(row[i][1])
        if(row[i][1] not in u_email):
            u_email.append(row[i][1])
        msg.append(row[i][2])
        if "OpenCV".lower() in msg[-1].lower():
            key_word.append("OpenCV")
        elif "Python".lower() in msg[-1].lower():
            key_word.append("Python")
        else:
            key_word.append("None")
    except ValueError:
        continue

today = datetime.now()
rec_date = []
for i in range(len(u_email)):
    dates = []
    for j in range(len(date)):
        if(u_email[i] == email[j]):
            dates.append(datetime.strptime(date[j], "%d/%m/%y"))
    rec_date.append(max(dates))
     
ALL_MAIL = pd.DataFrame({"Email ID" : email, "Email Message" : msg, "Date": date, "Key words" : key_word})
UNIQUE_MAIL = pd.DataFrame({"Email ID" : u_email, "Last date of conversation" : [i.strftime('%d/%m/%y') for i in rec_date], "Elapsed days" : [(today - rec_date[i]).days for i in range(len(u_email))]})

print("All mails : \n\n")
pretty_print_df(ALL_MAIL)

print("\n\nUnique mails with last date of conversation : \n\n")
pretty_print_df(UNIQUE_MAIL)

    





