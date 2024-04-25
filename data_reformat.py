# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:49:31 2024

@author: roboz
"""

import pandas as pd
import numpy as np

#Source metadata
# source = []
# platform = []
# original_size = []
# cleaned_size = []



#Importing Trump tweets
# trump = pd.read_csv('Data/trump_tweets/trump_tweets.csv')
# trump = trump[['text', 'datetime']]
# trump[['date', 'time']] = trump['datetime'].str.split('T', expand = True)
# trump[['year', 'month', 'day']] = trump['date'].str.split('-', expand = True).astype(int)
# trump[['hour', 'minute', 'second']] = trump['time'].str.split(':', expand = True)
# trump['hour'] = trump['hour'].astype(int)
# trump = trump[['text', 'year', 'month', 'day', 'hour']]



#Importing data
covid_data1 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Apr-Jun 2020).csv')
covid_data2 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Aug-Sep 2020).csv')
covid_data3 = pd.read_csv('Data/covid_tweets/Covid-19 Twitter Dataset (Apr-Jun 2021).csv')
covid_data_combined = pd.concat([covid_data1, covid_data2, covid_data3])
afghanistan = pd.read_csv('Data/Afghanistan_pd_with_Sentiments_Vader.csv')
biden_reelec = pd.read_csv('Data/biden_reelection_with_Sentiments_Vader.csv')
biden_t = pd.read_csv('Data/Biden_Tweets_with_Sentiments_Vader.csv')
biden_yt = pd.read_csv('Data/Biden_Youtube_with_Sentiments_Vader.csv')
impeach1 = pd.read_csv('Data/Impeached_pd_with_Sentiments_Vader_time .csv')
impeach2 = pd.read_csv('Data/Impeached_Sentiments_Vader.csv')
impeach = pd.concat([impeach1, impeach2])
trump_reelec = pd.read_csv('Data/trump_reelection_with_Sentiments_Vader.csv')
trump_t = pd.read_csv('Data/Trump_Tweets_with_Sentiments_Vader.csv')
trump_yt = pd.read_csv('Data/Youtube_trump_df_with_Sentiments_Vader.csv')



#Treating data
#Covid
#source.append('Covid tweets (0)')
#platform.append('Twitter (0)')
covid_data_combined.dropna(subset=['created_at'], inplace = True)
covid_data_combined[['year', 'month', 'day']] = covid_data_combined['created_at'].str.split('-', expand = True).astype(int)
covid_data_combined['hour'] = np.nan
covid_data_combined['minute'] = np.nan
covid_data_combined['second'] = np.nan
covid_data_combined['total_sentiment'] = covid_data_combined['pos'] - covid_data_combined['neg']
dropping = ['created_at', 'id', 'source', 'original_text', 'lang', 'favorite_count', 'retweet_count', 'original_author', 'hashtags', 'user_mentions', 'compound', 'sentiment', 'neu', 'neg', 'pos']
covid_data_combined = covid_data_combined.drop(dropping, axis=1)
covid_data_combined['dataset_id'] = 0
covid_data_combined['platform'] = 0
covid_data_combined = covid_data_combined[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]
#cleaned_size.append(len(covid_data_combined))

#Afghanistan
afghanistan[['date', 'time']] = afghanistan['Published At'].str.split('T', expand = True)
afghanistan['time'] = afghanistan['time'].str.replace('Z', '')
afghanistan[['year', 'month', 'day']] = afghanistan['date'].str.split('-', expand = True)
afghanistan[['hour', 'minute', 'second']] = afghanistan['time'].str.split(':', expand = True)
afghanistan.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
afghanistan[['year', 'month', 'day', 'hour', 'minute', 'second']] = afghanistan[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
afghanistan['clean_tweet'] = afghanistan['Comment']
afghanistan['total_sentiment'] = afghanistan['Sentiment']
afghanistan['dataset_id'] = 1
afghanistan['platform'] = 1
afghanistan['place'] = np.nan
afghanistan = afghanistan[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Biden Tweets
biden_t['place'] = biden_t['state']
biden_t['clean_tweet'] = biden_t['ClearTweet']
biden_t['total_sentiment'] = biden_t['SentimentScore']
biden_t['dataset_id'] = 2
biden_t['platform'] = 0
biden_t[['year', 'month', 'day', 'hour', 'minute', 'second']] = np.nan
biden_t = biden_t[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Biden Youtube
biden_yt['total_sentiment'] = biden_yt['Video Title'].shift(-1)
biden_yt.dropna(subset=['Video ID'], inplace = True)
biden_yt[['date', 'time']] = biden_yt['Published At'].str.split('T', expand = True)
biden_yt['time'] = biden_yt['time'].str.replace('Z', '')
biden_yt[['year', 'month', 'day']] = biden_yt['date'].str.split('-', expand = True)
biden_yt[['hour', 'minute', 'second']] = biden_yt['time'].str.split(':', expand = True)
biden_yt.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
biden_yt[['year', 'month', 'day', 'hour', 'minute', 'second']] = biden_yt[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
biden_yt['clean_tweet'] = biden_yt['Comment']
biden_yt['dataset_id'] = 3
biden_yt['platform'] = 1
biden_yt['place'] = np.nan
biden_yt = biden_yt[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]


#Biden reelection
biden_reelec[['date', 'time']] = biden_reelec['Published At'].str.split('T', expand = True)
biden_reelec['time'] = biden_reelec['time'].str.replace('Z', '')
biden_reelec[['year', 'month', 'day']] = biden_reelec['date'].str.split('-', expand = True)
biden_reelec[['hour', 'minute', 'second']] = biden_reelec['time'].str.split(':', expand = True)
biden_reelec.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
biden_reelec[['year', 'month', 'day', 'hour', 'minute', 'second']] = biden_reelec[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
biden_reelec['clean_tweet'] = biden_reelec['Comment']
biden_reelec['total_sentiment'] = biden_reelec['Sentiment']
biden_reelec['dataset_id'] = 4
biden_reelec['platform'] = 1
biden_reelec['place'] = np.nan
biden_reelec = biden_reelec[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Impeachment
impeach[['date', 'time']] = impeach['Timestamp'].str.split('T', expand = True)
impeach['time'] = impeach['time'].str.replace('Z', '')
impeach[['year', 'month', 'day']] = impeach['date'].str.split('-', expand = True)
impeach[['hour', 'minute', 'second']] = impeach['time'].str.split(':', expand = True)
impeach.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
impeach[['year', 'month', 'day', 'hour', 'minute', 'second']] = impeach[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
impeach['clean_tweet'] = impeach['Comment']
impeach['total_sentiment'] = impeach['Sentiment']
impeach['dataset_id'] = 5
impeach['platform'] = 1
impeach['place'] = np.nan
impeach = impeach[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Trump Tweets
trump_t['place'] = trump_t['state']
trump_t['clean_tweet'] = trump_t['ClearTweet']
trump_t['total_sentiment'] = trump_t['SentimentScore']
trump_t['dataset_id'] = 6
trump_t['platform'] = 0
trump_t[['year', 'month', 'day', 'hour', 'minute', 'second']] = np.nan
trump_t = trump_t[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Trump Youtube
trump_yt[['date', 'time']] = trump_yt['Published At'].str.split('T', expand = True)
trump_yt['time'] = trump_yt['time'].str.replace('Z', '')
trump_yt[['year', 'month', 'day']] = trump_yt['date'].str.split('-', expand = True)
trump_yt[['hour', 'minute', 'second']] = trump_yt['time'].str.split(':', expand = True)
trump_yt.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
trump_yt[['year', 'month', 'day', 'hour', 'minute', 'second']] = trump_yt[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
trump_yt['clean_tweet'] = trump_yt['Comment']
trump_yt['total_sentiment'] = trump_yt['Sentiment']
trump_yt['dataset_id'] = 7
trump_yt['platform'] = 1
trump_yt['place'] = np.nan
trump_yt = trump_yt[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]

#Trump reelection
trump_reelec[['date', 'time']] = trump_reelec['Published At'].str.split('T', expand = True)
trump_reelec['time'] = trump_reelec['time'].str.replace('Z', '')
trump_reelec[['year', 'month', 'day']] = trump_reelec['date'].str.split('-', expand = True)
trump_reelec[['hour', 'minute', 'second']] = trump_reelec['time'].str.split(':', expand = True)
trump_reelec.dropna(subset=['year', 'month', 'day', 'hour', 'minute', 'second'], inplace = True)
trump_reelec[['year', 'month', 'day', 'hour', 'minute', 'second']] = trump_reelec[['year', 'month', 'day', 'hour', 'minute', 'second']].astype(int)
trump_reelec['clean_tweet'] = trump_reelec['Comment']
trump_reelec['total_sentiment'] = trump_reelec['Sentiment']
trump_reelec['dataset_id'] = 8
trump_reelec['platform'] = 1
trump_reelec['place'] = np.nan
trump_reelec = trump_reelec[['dataset_id', 'platform', 'place', 'year', 'month', 'day', 'hour', 'minute', 'second', 'total_sentiment', 'clean_tweet']]



#Combining the datasets and exporting the full dataframe along with the source stats
right_ans = 0
while right_ans == 0:
    user = input('Would you like to include the covid dataset in the master dataset? (Y/N): ')
    #With covid dataset
    if user.upper() == 'Y':
        master = pd.concat([covid_data_combined, afghanistan, biden_t, biden_yt, biden_reelec, impeach, trump_t, trump_yt, trump_reelec])
        right_ans = 1
    #Without covid dataset
    elif user.upper() == 'N':
        master = pd.concat([afghanistan, biden_t, biden_yt, biden_reelec, impeach, trump_t, trump_yt, trump_reelec])
        right_ans = 1

# metadata = pd.DataFrame({'source':source, 'platfrom':platform, 'original_size':original_size, 'cleaned_size':cleaned_size})
# metadata.to_csv('metadata.csv')
# trump.to_csv('trump_reformat.csv')
master.to_csv('master.csv')