# test moar moar moar moar moar moar moar
from sopel import module

@module.commands('echo')
def echo(bot, trigger):
    bot.reply(trigger.group(2))
