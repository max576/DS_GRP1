import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Assuming Biden_Tweets DataFrame is prepared and contains the cleaned tweets

def get_sentiment(text):
    score = sia.polarity_scores(str(text))
    return score['compound']

# Apply the sentiment analysis to each tweet and create a new column for the sentiment score
Impeached_pd['Sentiment'] = Impeached_pd['Comment'].apply(get_sentiment)
print(Impeached_pd.head())

# Save the DataFrame with the sentiment scores to a new CSV file
Impeached_pd.to_csv('Impeached_Sentiments_Vader.csv', index=False)

print(Impeached_pd['Sentiment'])
