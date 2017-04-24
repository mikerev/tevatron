#!/usr/bin/env python
import praw, random, sys
from sopel import module
from time import sleep

clientID = 'CLIENTID'
clientSEC = 'CLIENTSECRET'
userAGNT = 'USERAGENT'

# @module.rule('')
# def hi(bot, trigger):
#     #sleep(random.randint(2,10))
#     if trigger.nick == 'Toba':
#        reddit = praw.Reddit(client_id=clientID, client_secret=clientSEC, user_agent=userAGNT)
#        subreddit = reddit.subreddit('chicago')
#        random_post_number = random.randint(0,100)
#        posts = subreddit.new(limit=1)
#        for i,post in enumerate(posts):
#            if i==random_post_number:
#                submission = reddit.submission(id=post.id)
#                for top_level_comment in submission.comments:
#                    comments = top_level_comment.body.splitlines()
#                    bot.say(random.choice(comments))
#                    break

@module.rule('Tevatron:')
def tevatron(bot, trigger):
    reddit = praw.Reddit(client_id=clientID, client_secret=clientSEC, user_agent=userAGNT)
    subreddit = reddit.subreddit('chicago')
    random_post_number = random.randint(0,100)
    posts = subreddit.new(limit=100)
    for i,post in enumerate(posts):
        if i==random_post_number:
            submission = reddit.submission(id=post.id)
            for top_level_comment in submission.comments:
                comments = top_level_comment.body.splitlines()
                bot.say(trigger.nick + ': ' + random.choice(comments))
                break


