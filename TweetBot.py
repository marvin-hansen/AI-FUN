import os

import tweepy
from time import sleep
import threading
import time
import sys

import KeyManager as k

from tweepy.error import TweepError

WAIT_TIME = 20
done = False

DBG = True

def authenticate_api():

    consumer_key, consumer_secret, access_token, access_secret = k.set_key(k.KEYS.TWITTER)
    print('Connecting to Twitter...')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    print('Connected!\n')
    return api


def read_text(file_name):
    my_file = open(file_name, 'r')

    file_lines = my_file.readlines()

    my_file.close()
    return file_lines


def update_text(file_name, line):
    with open(file_name, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != line:
                f.write(i)
        f.truncate()


def create_tweet_log(file_name):
     my_file = open(file_name, "w+")
     my_file.write("Tweet Log %d" "\r\n")
     my_file.close()


def log_tweets(file_name, line):

    exists: bool = os.path.isfile(file_name)
    if not exists:
        create_tweet_log(file_lines)


    my_file = open(file_name,"a+")
    # append tweet
    my_file.write(line + "\r\n")
    my_file.close()


if __name__ == '__main__':

    sleep_time_sec = 100
    hashtags =""
    author_name = " - Socrates.ai"
    file_name = "socrates-ai.txt"
    log_file = "already_tweeted.txt"

    file_lines = read_text(file_name)

    api = authenticate_api()

    for line in file_lines:
        # Add try ... except block to catch and output errors
        try:
            if line != '\n':
                if DBG: print("Tweeting: " + line)
                api.update_status(line+author_name)
                if DBG: print("updating text")
                update_text(file_name, line)
                if DBG: print("Logging tweet")
                log_tweets(log_file, line)

                sleep(sleep_time_sec)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(5)