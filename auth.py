# imports
from pickle import TRUE
import tweepy
import configparser

# tweepy doc
docLink = f'https://docs.tweepy.org/en/stable/api.html'

# config pasrser setup
config = configparser.ConfigParser()
config.read('./TwitterDev/config.ini')

# setting up auth keys
API_KEY = config['Twitter Developer']['API_KEY']
API_KEY_SECRET = config['Twitter Developer']['API_KEY_SECRET']
ACCESS_TOKEN = config['Twitter Developer']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['Twitter Developer']['ACCESS_TOKEN_SECRET']

# tweepy authentication
auth = tweepy.OAuth1UserHandler(
   API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
API = tweepy.API(auth, wait_on_rate_limit=TRUE)
