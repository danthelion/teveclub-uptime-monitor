Heroku deployment

1. Set variables

```shell
heroku config:set TWITTER_CONSUMER_KEY=xx
heroku config:set TWITTER_CONSUMER_SECRET=xx
heroku config:set TWITTER_ACCESS_TOKEN=xx
heroku config:set TWITTER_ACCESS_TOKEN_SECRET=xx
```

2. Install scheduler

```shell
heroku addons:create scheduler:standard
```

3. Test

```shell
heroku run python main.py
```

4. Create schedule

```shell
heroku addons:open scheduler
```