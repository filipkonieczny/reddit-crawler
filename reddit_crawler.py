#!/usr/bin/env python
# encoding: utf-8


# TODO: Description.
# Description.


# Imports.
import sys


# Constants.
DEFAULT_CRAWLING_DEPTH = 1


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

        pass

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

    # TODO: Validation code, du-uh?
    try:
        crawling_depth = int(crawling_depth)
    except ValueError:
        return False

    return True


def create_crawler(subreddit, crawling_depth):
    # TODO: Description.
    '''
    '''

    return RedditCrawler(subreddit, crawling_depth)


def crawl_subreddit(crawler):
    # TODO: Description.
    '''
    '''

    pass


def save_data(crawler):
    # TODO: Description.
    '''
    '''

    pass


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

    # TODO: Display 'hello message'.

    # TODO: Implement statistics, like:
    # 1. How much time it took,
    # 2. How many pages were crawled, etc.

    # 1) Get subreddit and crawling depth.
    subreddit = get_subreddit(sys.argv)
    if not validate_subreddit(subreddit):
        print "Oops, looks like you didn't provide a valid subreddit! :(\n"
        print 'Abort mission, I repeat: abort mission!!'
        return
    print 'Subreddit provided: {}'.format(subreddit)

    crawling_depth = get_crawling_depth(sys.argv)
    if not validate_crawling_depth(crawling_depth):
        print "Crawling depth not supplied or invalid! :("
        crawling_depth = DEFAULT_CRAWLING_DEPTH
    print "I'm gonna crawl {} pages for you!".format(crawling_depth)

    # 2) Crawl subreddit.
    reddit_crawler = create_crawler(subreddit, crawling_depth)
    crawl_subreddit(reddit_crawler)

    # 3) Save crawled data.
    save_data(reddit_crawler)


# Run the main function when executed from the command line.
if __name__ == "__main__":
    main()
