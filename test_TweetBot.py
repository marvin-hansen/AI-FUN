import pytest
from TweetBot import *
import KeyManager as k


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_authenticate_api():
    consumer_key, consumer_secret, access_token, access_secret = k.set_key(k.KEYS.TWITTER)
    api = authenticate_api(consumer_key, consumer_secret, access_token, access_secret )
    assert api is not None


def test_read_text():
    file_name = "socrates-ai.txt"
    file_lines = read_text(file_name)

    for line in file_lines:
        if line != '\n':
            assert line is not None


def test_update_text():
    pass


def test_create_tweet_log():
    file_name = "test_tweets.log"

    create_tweet_log(file_name)

    assert os.path.isfile(file_name)
    # cleanup after test
    os.remove(file_name)


def test_log_tweets():
    log_file = "test_tweets.log"
    line = "sample tweet"

    log_tweets(log_file, line)
    assert os.path.isfile(file_name)
    os.remove(log_file)





























