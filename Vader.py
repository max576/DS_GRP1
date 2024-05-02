import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
def get_sentiment(text):
    score = sia.polarity_scores(str(text))
    return score['compound']

Impeached_pd['Sentiment'] = Impeached_pd['Comment'].apply(get_sentiment)
print(Impeached_pd.head())

Impeached_pd.to_csv('Impeached_Sentiments_Vader.csv', index=False)

print(Impeached_pd['Sentiment'])
