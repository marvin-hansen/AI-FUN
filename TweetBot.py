import os

import tweepy
from time import sleep
from datetime import datetime

import KeyManager as k


WAIT_TIME = 20
done = False

DBG = True

def authenticate_api():
    """
    Authenticates against the official Twitter API and returns and api object 
    :return: api object
    """
    consumer_key, consumer_secret, access_token, access_secret = k.set_key(k.KEYS.TWITTER)
    print('Connecting to Twitter...')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    print('Connected!\n')
    return api


def read_text(file_name):
    """
    Reads tweets from a text file
    :param file_name: 
    :return: content of text file, line by line
    """
    my_file = open(file_name, 'r')

    file_lines = my_file.readlines()

    my_file.close()
    return file_lines


def update_text(file_name, line):
    """
    Removes a tweet from text file to prevent double posting
    :param file_name:
    :param line:
    :return: void
    """
    with open(file_name, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != line:
                f.write(i)
        f.truncate()


def create_tweet_log(file_name):
    """
    Creates tweet log file to store posts already tweeted.
    :param file_name:
    :return: void
    """
    my_file = open(file_name, "w+")
    my_file.write("Tweet Log %d" "\r\n")
    my_file.close()


def log_tweets(file_name, line):
    """
    Logs tweets in a text file with timestamp
    :param file_name:
    :param line:
    :return: void
    """

    exists: bool = os.path.isfile(file_name)
    if not exists:
        create_tweet_log(file_lines)

    my_file = open(file_name,"a+")
    # create timestamp
    timestamp = datetime.timestamp(datetime.now())
    # append tweet with time stamp
    my_file.write(str(timestamp) + ":" + line + "\r\n")
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