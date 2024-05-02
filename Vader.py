import pandas as pd

Youtube_trump_df = pd.read_csv(r"/kaggle/input/trumpyt/all_trump_youtube_comments.csv")

Youtube_biden_df = pd.read_csv(r"/kaggle/input/youtubecomments/youtube/all_biden_youtube_comments.csv",lineterminator='\n')

Impeached_pd = pd.read_csv("/kaggle/working/impeachment.csv")

Afghanistan_pd = pd.read_csv("/kaggle/input/afghanistan/afghanistan_comments.csv")

TrumpImpeachmentSpeach = pd.read_csv("/kaggle/working/TrumpImpeachmentSpeech.csv")

Riots = pd.read_csv("/kaggle/input/trump-riots-and-tweets/capitol_riots_tweets.csv")

TrumpTweets = pd.read_csv("/kaggle/input/trump-riots-and-tweets/trump_tweets.csv")

trump_reelection = pd.read_csv("/kaggle/input/reelection/trump_reelection.csv")

biden_reelection = pd.read_csv("/kaggle/input/reelection/biden_reelection.csv")


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
