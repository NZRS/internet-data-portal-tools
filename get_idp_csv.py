
import pandas as pd  
import numpy as np 
import time


idp_url = 'https://idp.nz/api/views/mm2r-3dj9/rows.csv'


# Year, month and day columns functions


def get_day(date_string):  
    return date_string[:2]

def get_month(date_string):  
    return date_string[3:5]

def get_year(date_string):  
    return date_string[6:10]

my_frame = pd.read_csv(idp_url)  


#Create three new columns using previously defined functions
my_frame['day'] = my_frame['Day'].apply(get_day)  
my_frame['month'] = my_frame['Day'].apply(get_month)  
my_frame['year'] = my_frame['Day'].apply(get_year)


# Add a YRMO number
my_frame['yrmo'] = my_frame['year'] + my_frame['month']

# Save as csv

## dd-mm-yyyy format
out_file = 'idp' + str((time.strftime("%d-%m-%Y"))) + '.csv'

my_frame.to_csv(out_file)
