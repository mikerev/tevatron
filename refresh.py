#!/usr/bin/env python
import subprocess
from sopel import module
repo_dir = '/home/tevatron/custom_modules'

@module.rule('.refresh')
def hi(bot, trigger):
    subprocess.call('cd %s && git pull', shell=True)
    bot.say(trigger.nick + ': Done!')

