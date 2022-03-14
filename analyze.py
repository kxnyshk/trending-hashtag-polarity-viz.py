# local imports
from auth import API
from time import sleep

# module imports
import re
import sys
import tweepy
import textblob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# constants
lag = 0.05

# writer
def writer(text):
    for char in text:
        sleep(lag)
        sys.stdout.write(char)
        sys.stdout.flush()

# analyzing

def analyze(hash):

    writer(f'\nWait while we fetch the #{hash} sentiment analysis for you ..')

    # query
    q_ = f'#{hash} -filter:retweets'

    # cursor setup
    items_ = 1000
    tweet_cursor = tweepy.Cursor(API.search_tweets, q=q_, lang = 'en', tweet_mode = 'extended').items(items_)

    # fetching
    tweets = [tweet.full_text for tweet in tweet_cursor]

    # df setup
    tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

    # cleaning tweet text
    for _, row in tweets_df.iterrows():
        row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
        row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
        row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
        row['Tweets'] = re.sub('\\n', '', row['Tweets'])

    # mapping polarity
    tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
    tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

    ## analyzing
    pos = tweets_df[tweets_df.Result == '+'].count()['Tweets']
    neg = tweets_df[tweets_df.Result == '-'].count()['Tweets']

    # print analysis
    def analysis():

        total = (pos+neg)
        pos_percent = round(((pos/total) * 100), 2)
        neg_percent = round(((neg/total) * 100), 2)

        print(f'\nHashtag: #{hash}')
        print(f'Positive sentiments: {pos_percent}%')
        print(f'Negative sentiments: {neg_percent}%')
        print(f'\nTotal dataset scope: {total} users')

    # plotting
    def plot():

        pos_color = '#0ce8a2'
        neg_color = '#e31941'

        plt.bar([0, 1], [pos, neg], width=1, label=['Positive', 'Negative'], color=[pos_color, neg_color])
        plt.legend()

        plt.show()

    # run
    def run():

        try:
            if((pos > 10) or (neg > 10)):
                analysis()
                plot()

        except:
            ERR = f'Oops! Too less tweets on this #{hash}'
            print(ERR)
    
    run()
