from sopel import *
import random

qdb = "/home/tevatron/tevatron/custom_modules/karma.db"

@module.commands('karma')
@module.example('.karma boobs')
def karma(bot, trigger):
        karma = trigger.group(2)
        f = open(qdb, 'a')
        f.write("\n%s" % karma)
        f.close()
        bot.reply('Added it...')

@module.commands('karma')
@module.example('.karma')
def karma(bot, trigger):
	search = trigger.group(2)
        f = open(qdb, 'r')
	if search < 0:
            line = random.choice(list(open(qdb)))
            bot.reply(line)

