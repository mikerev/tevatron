from sopel import module
import random

tardbase = "/home/tevatron/custom_modules/crazytard.txt"

@module.rule('')
def tard(bot, trigger):
    if trigger.nick == 'CrazyMug':
        f = open(tardbase, 'r')
        line = random.choice(list(open(tardbase)))
        bot.say(line)
