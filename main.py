import os

import dotenv
import requests
import tweepy


def check_if_tc_is_up() -> int:
    r = requests.get("https://www.teveclub.hu/", timeout=5)
    return r.status_code


def post_tweet() -> None:
    client = tweepy.Client(**read_dotenv_dict())
    client.create_tweet(text=f"TeveClub is {'🥰' if check_if_tc_is_up() == 200 else '😭'}", media_ids=None)


def read_dotenv_dict() -> dict:
    dotenv.load_dotenv()
    return {
        "consumer_key": os.getenv("TWITTER_CONSUMER_KEY"),
        "consumer_secret": os.getenv("TWITTER_CONSUMER_SECRET"),
        "access_token": os.getenv("TWITTER_ACCESS_TOKEN"),
        "access_token_secret": os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    }


if __name__ == '__main__':
    post_tweet()
