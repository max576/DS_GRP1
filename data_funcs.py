# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:35:08 2024

@author: roboz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import textfunctions_for_dash as tf

#trump

def displays(input1, input2, data):
    
    #Defining the filter(s) as lists
    filter1 = input1.split(' ')
    filter2 = input2.split(' ')
    compare_bool = int(filter1[0]) - 1
    filter1 = filter1[1:]
    columns = ['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minutes', 'seconds', 'total_sentiment']
    all_index1 = []
    
    #Creating df1
    df1 = data.copy()
    for i in range(0, 9):
        if filter1[i] != 'all':
            filter1[i] = int(filter1[i])
            df1 = df1.drop(df1[df1[columns[i]] != filter1[i]].index)
            
    #Filtering sentiment
    if filter1[9] != 'all':
        sent = float(filter1[9])
        if sent == 0:
            df1 = df1.drop(df1[df1['total_sentiment'] < -0.1].index)
            df1 = df1.drop(df1[df1['total_sentiment'] > 0.1].index)
        elif sent < 0:
            df1 = df1.drop(df1[(sent - 0.1) > df1['total_sentiment']].index)
            df1 = df1.drop(df1[sent < df1['total_sentiment']].index)
        elif sent > 0:
            df1 = df1.drop(df1[(sent + 0.1) < df1['total_sentiment']].index)
            df1 = df1.drop(df1[sent > df1['total_sentiment']].index)
        elif sent == 1 or sent == -1:
            df1 = df1.drop(df1[df1['total_sentiment'] != sent].index)
    
    
    #Dealing with no comparing
    if compare_bool == 0:
        print('No compare!')
        
        #Plotting and computing
        #Sentiment distribution
        plt.hist(df1['total_sentiment'], bins = 21, density = True)
        plt.xlabel('Sentiment')
        plt.ylabel('Probability Density')
        plt.title('Sentiment Distribution')
        plt.show()
        
        #Temporal plot
        for i in range(3, 9):
            if filter1[i] == 'all':
                all_index1.append(i)
        
        if len(all_index1) > 0:
            x_axis = all_index1[0]
        else:
            x_axis = 8
        df1_dropped = df1.dropna(subset = [columns[x_axis]])
        sentiment1 = df1_dropped.groupby(columns[x_axis])['total_sentiment'].mean()
        plt.bar(sentiment1.index, sentiment1.values)
        plt.xlabel('Time (' + columns[x_axis] + 's)')
        plt.ylabel('Average Sentiment')
        plt.title('Sentiment Over Time')
        plt.show()
        
        #Word clouds
        tf.mostpopularwordcloud(df1)
        tf.mostpopularbigrams(df1)
        tf.mostpopulartrigrams(df1)
        
        
        #Descriptive stats
        list1 = df1['total_sentiment'].tolist()
        size1 = len(list1)
        mu1 = sum(list1) / size1
        sigma1 = np.std(list1)
        skew1 = skew(list1)
        used_ratio1 = (len(df1_dropped['total_sentiment']) / size1)*100
        
        print('The mean sentiment for this timeframe is: ' + str(mu1))
        print('The standard deviation for this timeframe is: ' + str(sigma1))
        print('The skew for this timeframe is: ' + str(skew1))
        print('The original size of this data subset was: ' + str(size1))
        print('The amount of usable data used in the Sentiment Over Time plot is: ' + str(used_ratio1) + '%')
        
        return df1, 'No dataframe'
    
    
    
    
    
    
    
    
    #Dealing with yes comparing
    elif compare_bool == 1:
        print('Yes compare!')
        
        #Creating df2
        df2 = data.copy()
        for i in range(0, 9):
            if filter2[i] != 'all':
                filter2[i] = int(filter2[i])
                df2 = df2.drop(df2[df2[columns[i]] != filter2[i]].index)   
        
        #Filtering sentiment
        if filter2[9] != 'all':
            sent = float(filter2[9])
            if sent == 0:
                df1 = df1.drop(df1[df1['total_sentiment'] < -0.1].index)
                df1 = df1.drop(df1[df1['total_sentiment'] > 0.1].index)
            elif sent < 0:
                df1 = df1.drop(df1[(sent - 0.1) > df1['total_sentiment']].index)
                df1 = df1.drop(df1[sent < df1['total_sentiment']].index)
            elif sent > 0:
                df1 = df1.drop(df1[(sent + 0.1) < df1['total_sentiment']].index)
                df1 = df1.drop(df1[sent > df1['total_sentiment']].index)
            elif sent == 1 or sent == -1:
                df1 = df1.drop(df1[df1['total_sentiment'] != sent].index)  
        
        #Plotting and computing
        #Sentiment distribution
        plt.hist(df1['total_sentiment'], bins = 21, density = True, alpha = 0.85)
        plt.hist(df2['total_sentiment'], bins = 21, density = True, alpha = 0.4, color = 'red')
        plt.legend(labels = ['Dataset 1', 'Dataset 2'])
        plt.xlabel('Sentiment')
        plt.ylabel('Probability Density')
        plt.title('Sentiment Distribution')
        plt.show()
        
        #Temporal plot
        for i in range(3, 9):
            if filter1[i] == 'all':
                all_index1.append(i)
        
        if len(all_index1) > 0:
            x_axis = all_index1[0]
        else:
            x_axis = 8
        df1_dropped = df1.dropna(subset = [columns[x_axis]])
        df2_dropped = df2.dropna(subset = [columns[x_axis]])
        sentiment1 = df1_dropped.groupby(columns[x_axis])['total_sentiment'].mean()
        sentiment2 = df2_dropped.groupby(columns[x_axis])['total_sentiment'].mean()
        plt.bar(sentiment1.index, sentiment1.values, alpha = 0.85)
        plt.bar(sentiment2.index, sentiment2.values, alpha = 0.4, color = 'red')
        plt.legend(labels = ['Dataset 1', 'Dataset 2'])
        plt.xlabel('Time (' + columns[x_axis] + 's)')
        plt.ylabel('Average Sentiment')
        plt.title('Sentiment Over Time')
        plt.show()
        
        #Word clouds
        print('Word cloud stuff for dataset 1')
        tf.mostpopularwordcloud(df1)
        tf.mostpopularbigrams(df1)
        tf.mostpopulartrigrams(df1)
        print('Word cloud stuff for dataset 2')
        tf.mostpopularwordcloud(df2)
        tf.mostpopularbigrams(df2)
        tf.mostpopulartrigrams(df2)
        
        #Descriptive stats
        list1 = df1['total_sentiment'].tolist()
        list2 = df2['total_sentiment'].tolist()
        size1 = len(list1)
        size2 = len(list2)
        mu1 = sum(list1) / size1
        mu2 = sum(list2) / size2
        sigma1 = np.std(list1)
        sigma2 = np.std(list2)
        skew1 = skew(list1)
        skew2 = skew(list2)
        used_ratio1 = (len(df1_dropped['total_sentiment']) / size1)*100
        used_ratio2 = (len(df2_dropped['total_sentiment']) / size2)*100
        
        print('Dataset 1')
        print('The mean sentiment for this timeframe is: ' + str(mu1))
        print('The standard deviation for this timeframe is: ' + str(sigma1))
        print('The skew for this timeframe is: ' + str(skew1))
        print('The original size of this data subset was: ' + str(size1))
        print('The amount of usable data used in the Sentiment Over Time plot is: ' + str(used_ratio1) + '%')
        
        print('Dataset 2')
        print('The mean sentiment for this timeframe is: ' + str(mu2))
        print('The standard deviation for this timeframe is: ' + str(sigma2))
        print('The skew for this timeframe is: ' + str(skew2))
        print('The original size of this data subset was: ' + str(size2))
        print('The amount of usable data used in the Sentiment Over Time plot is: ' + str(used_ratio2) + '%')
        
        return df1, df2
    
    
    #Extras
    elif compare_bool > 1:
        print('Too much compare!')
        
    else:
        print('Bad compare!')