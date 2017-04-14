#!/usr/bin/env python
import praw, random, sys

reddit = praw.Reddit(client_id='CLIENTID', client_secret='CLIENTSECRET', user_agent='USERAGENT')

subreddit = reddit.subreddit('chicago')
random_post_number = random.randint(0,100)
posts = subreddit.new(limit=100)

for i,post in enumerate(posts):
    if i==random_post_number:
        submission = reddit.submission(id=post.id)
        for top_level_comment in submission.comments:
            comments = top_level_comment.body.splitlines()
            print random.choice(comments)
            break