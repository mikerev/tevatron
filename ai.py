#!/usr/bin/env python
from textblob import TextBlob
import re
import textblob.download_corpora
import praw, random, sys
from time import sleep
from itertools import islice
from nltk import sent_tokenize
import os

clientID = os.environ["TEVATRON_CLIENT_ID"]
clientSEC = os.environ["TEVATRON_CLIENT_KEY"]
userAGNT = os.environ["TEVATRON_CLIENT_AGENT"]

raw_log = '/home/tevatron/.sopel/logs/default.raw.log'

noun_filter = ['http', 'deleted']

def main():
    posts = get_posts()
    for msg_noun in get_msg_nouns():
        for p_id,post in enumerate(posts):
            if msg_noun in post:
                print('hit: ' + msg_noun + ' from: ' + post)
            
def get_post_nouns():
    posts = get_posts()
    post_nouns = []
    for post in posts:
        blob = TextBlob(post)
        nouns = blob.noun_phrases
        print(nouns)
        for n in nouns: 
            clean_nouns = re.match('^[A-Za-z0-9.,:;!?()\s]+$', n)
            if clean_nouns:
                if not any(s in n for s in noun_filter):
                    post_nouns.append(n)

    return post_nouns


def get_msg_nouns():
    msgs = get_msgs()
    msg_nouns = []
    for msg in get_msgs():
        blob = TextBlob(msg)
        nouns = blob.noun_phrases
        for n in nouns:
            clean_nouns = re.match('^[A-Za-z0-9.,:;!?()\s]+$', n)
            if clean_nouns:
                if not any(s in n for s in noun_filter):
                    msg_nouns.append(n)
    return msg_nouns
                        

def get_posts():
    reddit_posts = []
    reddit = praw.Reddit(client_id=clientID,
                         client_secret=clientSEC, 
                         user_agent=userAGNT)
    subreddit = reddit.subreddit('chicago')
    random_post_number = random.randint(0,100)
    posts = subreddit.new(limit=100)
    for i,post in enumerate(posts):
        for c in post.comments:
            line = c.body.encode('ascii', 'ignore').decode('ascii')
            if not any(s in line for s in noun_filter):
                reddit_posts.append(line)
    return reddit_posts

def get_msgs():
    msgs = []
    with open(raw_log, 'rb') as f:
        for line in f:
            line = str(f.readline().rstrip())
            if 'PRIVMSG #' in line:
                if 'unregged' not in line:
                    l = line.split(":", 2)
                    if len(l) > 2:
                        msgs.append(l[2])
    return msgs
    
main()
