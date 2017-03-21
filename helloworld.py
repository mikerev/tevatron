"""
helloworld.py : A sopel tutorial callable

Remember to say .helloworld
"""

import sopel
@sopel.module.commands('helloworld')

def helloworld(bot, trigger):
   bot.say('You and your world can go get fucked')

