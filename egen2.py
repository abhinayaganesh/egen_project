import tweepy
import pymongo
import datetime
import io 
import sys
import pytz
from pymongo import MongoClient
import json
import twitter
from pprint import pprint

consumer_key = "TqbTZEf7UL5yKuuIwNTFIR3sV"
consumer_secret = "bY3HtJfLi6hmBfaefRMSi8DQzNaIKdvIIJsAmDSLvwdkmoqSM0"
access_token = "4180437988-cKm4LNohEn1F7rY3DRIiPvGuaqAJdfQ6zuOhOsI"
access_token_secret = "Io9pva3uXQguf2P0w20p2aXbG70cXNuF6OSLrA2mwjHnZ"
MONGO_HOST= "mongodb://localhost:27017/"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

client = pymongo.MongoClient(MONGO_HOST)
db = client.twitter_db
collection = db.my_collection