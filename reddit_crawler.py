#!/usr/bin/env python
# encoding: utf-8


# The story behind this crawler is that I wanted to
# get all of http://www.reddit.com/r/dailyprogrammer/ challanges,
# but couldn't have been bothered to go through every post,
# page by page, for hundreds of posts.


# Imports.
from sys import argv
from time import time
import requests
import json


# Constants.
DEFAULT_CRAWLING_DEPTH = 1
DATA_FILE = 'data.json'


# Classes.
class RedditCrawler():
    # TODO: Description.
    '''
    '''

    def __init__(self, subreddit, crawling_depth):
        # TODO: Description.
        '''
        '''

        self.subreddit = subreddit
        self.crawling_depth = crawling_depth

    def crawl(self):
        # TODO: Description.
        '''
        '''

        r = requests.get(self.subreddit)

        self.data = r.json()

        # TEST:
        print (self.data)

    def crawl_page(self):
        # TODO: Description.
        '''
        '''

        pass

    def crawl_post(self):
        # TODO: Description.
        '''
        '''

        pass

    def crawl_first_comment(self):
        # TODO: Description.
        '''
        '''

        pass

    def return_data(self):
        # TODO: Description.
        '''
        '''

        pass


# Functions.
def get_subreddit(system_arguments):
    '''
    Extracts a subreddit from received system arguments.
    Returns 'None' if no sys.argv[1] supplied.

    ([strings]) -> string or None

    >>> get_subreddit(sys.argv)
    'http://www.reddit.com/r/dailyprogrammer/'

    '''

    if len(system_arguments) == 1:
        return None

    return system_arguments[1]


def validate_subreddit(subreddit):
    '''
    Validates received subreddit and returns a bool, accordingly.

    (string) -> bool

    >>> validate_subreddit('http://www.reddit.com/r/dailyprogrammer/')
    True

    '''

    if subreddit is None:
        return False

    if 'reddit.com/r/' in subreddit and '/comments/' not in subreddit:
        return True

    return False


def get_crawling_depth(system_arguments):
    '''
    Extracts crawling depth from received system arguments.
    Crawling depth defines how many pages of a given subreddit
    are meant to be crawled.
    Returns 'None' if no sys.argv[2] supplied.

    ([strings]) -> string or None

    >>> get_crawling_depth(sys.argv)
    '10'

    '''

    if len(system_arguments) < 3:
        return None

    crawling_depth = system_arguments[2]

    return crawling_depth


def validate_crawling_depth(crawling_depth):
    '''
    Validates received crawling depth and returns a bool, accordingly.

    (string) -> bool

    >>> validate_crawling_depth('10')
    True

    '''

    if crawling_depth is None:
        return False

    try:
        crawling_depth = int(crawling_depth)
    except ValueError:
        return False

    return True


def create_crawler(subreddit, crawling_depth):
    '''
    Creates a RedditCrawler instance.

    (string, int) -> RedditCrawler()

    >>> create_crawler('http://www.reddit.com/r/dailyprogrammer/', 10)
    <__main__.RedditCrawler instance at 0x7f731f74b710>

    '''

    return RedditCrawler(subreddit, crawling_depth)


def crawl_subreddit(crawler):
    '''
    Initiates crawling process.

    (RedditCrawler()) -> RedditCrawler().crawl()

    '''

    crawler.crawl()


def save_data(crawler):
    '''
    Saves the data stored in RedditCrawler().data into a .json file.

    (RedditCrawler()) -> DATA_FILE

    '''

    with open(DATA_FILE, 'w') as outfile:
        json.dump(crawler.data, outfile, indent=4)


def main():
    '''
    Main function is responsible for executing all other functions.
    Also takes care of human-computer interaction, like displaying messages.

    Crawling a subreddit is divided into 3 stages:
    1) Get subreddit and crawling depth*.
    * crawling_depth defines how many pages of a given subreddit
      are meant to be crawled.

    2) Crawl subreddit.

    3) Save crawled data and make anything you want with it.

    '''

    # Print 'Hello' message.
    print ('\nOhai!\n\nWelcome to Reddit Crawler - enjoy!\n\n')

    # TODO: Implement statistics, like:
    # 1. How many pages were crawled, etc.
    # Statistics.
    start = time()

    # 1) Get subreddit and crawling depth.
    subreddit = get_subreddit(argv)
    if not validate_subreddit(subreddit):
        print ("Oops, looks like you didn't provide a valid subreddit! :(\n")
        print ('Abort mission, I repeat: abort mission!!')
        return
    print ("Subreddit provided: '{}'".format(subreddit))

    crawling_depth = get_crawling_depth(argv)
    if not validate_crawling_depth(crawling_depth):
        print ("Crawling depth not supplied or invalid! :(")
        crawling_depth = DEFAULT_CRAWLING_DEPTH
    print ("I'm gonna crawl {} pages for you!".format(crawling_depth))

    # 2) Crawl subreddit.
    reddit_crawler = create_crawler(subreddit, crawling_depth)
    crawl_subreddit(reddit_crawler)

    # 3) Save crawled data.
    save_data(reddit_crawler)

    # Print statistics.
    stop = time()
    duration = stop - start
    print ('\nExecuted in {0:.2f} seconds!'.format(duration))

    # Print 'Goodbye' message.
    print ('\n\nThanks for using Reddit Crawler, cheers!\n')


# Run the main function when executed from the command line.
if __name__ == "__main__":
    main()
