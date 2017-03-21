from sopel import module
from random import choice

@module.rule('hello?')
def hi(bot, trigger):
    bot.say('Hi, ' + trigger.nick)

@module.rule('does anyone know')
def notgoogle(bot, trigger):
    bot.reply('Does this look like Google to you?') 

@module.rule('good morning everyone')
def morning(bot, trigger):
    bot.say('Good morning, ' + trigger.nick)

@module.rule('hi Tevatron')
def hi(bot, trigger):
    bot.say('Heya, ' + trigger.nick)
    
@module.rule('beekar')
def beek(bot, trigger):
    bot.say('Beekar is a stone cold pimp, %s!' % trigger.nick)

@module.rule('sup Tevatron')
def sup(bot, trigger):
    bot.say('What\'it do, mang.')

@module.rule('smoke weed')
def weed(bot, trigger):
    bot.say('errday.')
    
@module.rule('beer')
def beer(bot, trigger):
    bot.say('mmmm.....beeeeeer.')

@module.rule('Tevatron, what do you do?')
def profession(bot, trigger):
    bot.say('ERRDAY I\'M SPINNIN')

@module.rule('good morning, Tevatron')
def morningtev(bot, trigger):
    bot.say('Good morning, ' + trigger.nick)

@module.rule('bleh')
def beer(bot, trigger):
    bot.say('blorp')
    
@module.rule('good evening, Tevatron')
def eveningtev(bot, trigger):
    bot.say('Good evening, ' + trigger.nick)

@module.rule('puppy')
def puppy(bot, trigger):
    puppysays = ["Woof! Woof " + trigger.nick,
                 "Baconbaconbaconbaconbacon IT'S BACON!"]
    tag = choice(puppysays)
    bot.say("""     ,. """)
    bot.say("""      /  `-._ """)
    bot.say("""     /       `.     ___            __ """)
    bot.say("""   ,'       _/ ,---'   `-.       ,'  `. """)
    bot.say("""  /   /`---' \/           `--.  /      \ """)
    bot.say(""" /   |       /             _  `/  -.    `. """)
    bot.say(""" \   |              ,.    /O\  \    \     \ """)
    bot.say("""  \   `.           /O \  '   `. `. / \    | """)
    bot.say("""   `._  `-.       /   ,   .    ,  `.  \  ,' """)
    bot.say("""      `-.        .   /     `--'     \  \/ """)
    bot.say("""         \        `-',d8o8b.        / """)
    bot.say("""          \          dP'88`8b      / """)
    bot.say("""           \  ,'`.     `YP'       | """)
    bot.say("""          \/ .        |       | |         %s """ % tag)
    bot.say("""            /  |\       :       |/\ """)
    bot.say("""           /   | `.   ,:::     / \ \ """)
    bot.say("""          ,\       `-'`""'`.--'  )o ) """)
    bot.say("""         (o `.__,               / o/ """)
    bot.say("""          \ o   \_           ,-'o / """)
    bot.say("""           \  o  o`-----.__,' o ,' """)
    bot.say("""            `----. o  o  o  o ,' """)
    bot.say("""                  `----------' """)
    bot.say("""""")

