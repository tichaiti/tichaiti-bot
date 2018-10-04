#!/usr/bin/env python

import random
import re

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to


def main():
    bot = Bot()
    bot.run()


@respond_to('(sak*.ap*.fet)', re.IGNORECASE)
def sakapfet(ws, message):
    ws.reply('nap boule!')


@respond_to('(koman*.ou*.ye)', re.IGNORECASE)
def komanwye(ws, message):
    repons = ['nou la wi, nap genbe', 'nap byen pase', 'nou anfom...']
    ws.reply(random.choice(repons))


@listen_to('joined')
def bienvenue(ws):
    mesaj = ['Onè! Respè!', 'Bienvenue!', 'Welcome!']
    ws.reply(random.choice(mesaj))


if __name__ == "__main__":
    main()
