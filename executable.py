# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:48:02 2024

@author: roboz
"""

import pandas as pd
import data_funcs as df

#Importing data
trump = pd.read_csv('trump_reformat.csv')
data = pd.read_csv('combined_dataset.csv')

#Loop until exit
user_input = 'empty string'
input2 = 'empty string'
example = '1 all 0 all 2020 5 all all'
while user_input.upper() != 'EXIT':
    if user_input == 'empty string':
        print('You will be asked to input a filter or to exit. Please see the README for all valid values for each filter option')
        print('Here is an example of a filter you may use:')
        print(example)
        print('If you want use compare mode, you will be asked to input a second filter.')
        print('Here is an example of a secondary filter you may use:')
        print(example[2:])
    else:
        print('Your previous input was: ' + user_input)
    
    user_input = input('Please input a new filter or type "exit" to exit: ')
    if user_input.split(' ')[0] == '2':
        print('Here is your first filter: ' + user_input)
        input2 = input('Please input your second filter: ')
    try:
        df1, df2 = df.displays(user_input, input2, trump, data)
    except:
        if user_input.upper() == 'EXIT':
            print('Exiting')
        else:
            print('Invalid input')