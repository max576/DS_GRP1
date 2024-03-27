# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:49:31 2024

@author: roboz
"""

import pandas as pd
import numpy as np

#Source metadata
source = []
platform = []
original_size = []
cleaned_size = []



#Importing event data
trump = pd.read_csv('Data/trump_tweets/trump_tweets.csv')
trump = trump[['text', 'datetime']]
trump[['date', 'time']] = trump['datetime'].str.split('T', expand = True)
trump[['year', 'month', 'day']] = trump['date'].str.split('-', expand = True).astype(int)
trump[['hour', 'minute', 'second']] = trump['time'].str.split(':', expand = True)
trump['hour'] = trump['hour'].astype(int)
trump = trump[['text', 'year', 'month', 'day', 'hour']]



#Importing tweet data
covid_data1 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Apr-Jun 2020).csv')
covid_data2 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Aug-Sep 2020).csv')
covid_data3 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Apr-Jun 2021).csv')
covid_data_combined = pd.concat([covid_data1, covid_data2, covid_data3])
original_size.append(len(covid_data_combined))



#Treating data
#Covid dataset
source.append('Covid tweets (0)')
platform.append('Twitter (0)')
covid_data_combined.dropna(subset=['created_at'], inplace = True)
covid_data_combined[['year', 'month', 'day']] = covid_data_combined['created_at'].str.split('-', expand = True).astype(int)
covid_data_combined['hour'] = np.nan
covid_data_combined['total_sentiment'] = covid_data_combined['pos'] - covid_data_combined['neg']
dropping = ['created_at', 'id', 'source', 'original_text', 'lang', 'favorite_count', 'retweet_count', 'original_author', 'hashtags', 'user_mentions', 'compound', 'sentiment', 'neu', 'neg', 'pos']
covid_data_combined = covid_data_combined.drop(dropping, axis=1)
covid_data_combined['dataset_id'] = 0
covid_data_combined['platform'] = 0
covid_data_combined = covid_data_combined[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'total_sentiment', 'clean_tweet']]
cleaned_size.append(len(covid_data_combined))



#Combining the datasets and exporting the full dataframe along with the source stats

#COMBINE HERE

metadata = pd.DataFrame({'source':source, 'platfrom':platform, 'original_size':original_size, 'cleaned_size':cleaned_size})
metadata.to_csv('metadata.csv')
trump.to_csv('trump_reformat.csv')
covid_data_combined.to_csv('combined_dataset.csv')