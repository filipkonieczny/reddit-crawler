# Reddit Crawler

[Python](https://www.python.org/) script to crawl [Reddit](http://www.reddit.com/).


About
-----

The story behind this crawler is that I wanted to get all of [/r/DailyProgrammer/](http://www.reddit.com/r/dailyprogrammer/) challanges, but couldn't have been bothered to go through every post, page by page, for hundreds of posts.


Features
--------

- Crawl any subreddit,
- Choose how many pages you wish to crawl,
- Save crawled data and do whatever you want with it


Prerequisites
-------------
- [```Python``` 2.7+](https://www.python.org/download/releases/2.7/),
- [```virtualenv```](http://virtualenv.readthedocs.org/en/latest/),
- [```pip```](https://pypi.python.org/pypi/pip)


Setup
-----

```
$ git clone https://github.com/filipkonieczny/reddit-crawler.git
$ cd reddit-crawler/
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```


Usage
-----

All you have to do is run the script while in project directory like this:

```
$ python reddit_crawler.py SUBREDDIT CRAWLING_DEPTH
```

and supplying ```SUBREDDIT``` and ```CRAWLING_DEPTH```(optional, default is 1), for example:

```
$ python reddit_crawler.py http://www.reddit.com/r/dailyprogrammer/ 10
```

will crawl you first 10 pages of [/r/DailyProgrammer/](http://www.reddit.com/r/dailyprogrammer/) subreddit.
