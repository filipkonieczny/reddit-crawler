#!/usr/bin/env python
# encoding: utf-8


# TODO: description
# description


# imports
import sys


# constants


# classes
class RedditCrawler():
    # TODO: description
    '''
    '''

    def __init__(self):
        # TODO: description
        '''
        '''

        pass

    def crawl(self):
        # TODO: description
        '''
        '''

        pass

    def crawl_page(self):
        # TODO: description
        '''
        '''

        pass

    def return_data(self):
        # TODO: description
        '''
        '''

        pass


# functions
def get_subreddit(system_arguments):
    # TODO: description
    '''
    '''

    pass


def validate_subreddit(subreddit):
    # TODO: description
    '''
    '''

    pass


def get_crawling_depth(system_arguments):
    # TODO: description
    '''
    '''

    pass


def validate_crawling_depth(crawling_depth):
    # TODO: description
    '''
    '''

    pass


def create_crawler(subreddit, crawling_depth):
    # TODO: description
    '''
    '''

    pass


def crawl_subreddit(crawler):
    # TODO: description
    '''
    '''

    pass


def save_data(crawler):
    # TODO: description
    '''
    '''

    pass


def main():
    # TODO: description
    '''
    '''

    subreddit = get_subreddit(sys.argv)
    if not validate_subreddit(subreddit):
        pass

    crawling_depth = get_crawling_depth(sys.argv)
    if not validate_crawling_depth(crawling_depth):
        pass

    reddit_crawler = create_crawler(subreddit, crawling_depth)
    crawl_subreddit(reddit_crawler)
    save_data(reddit_crawler)


if __name__ == "__main__":
    main()
