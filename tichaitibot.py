#!/usr/bin/env python

import random
import re

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('hi', re.IGNORECASE)
def sayhi(ws):
    ws.reply('Koman ou ye?')


@respond_to('(sak*.ap*.fet)', re.IGNORECASE)
def sakapfet(ws, message):
    ws.reply('nap boule!')


@respond_to('(koman*.ou*.ye)', re.IGNORECASE)
def komanwye(ws, message):
    repons = ['nou la wi, nap genbe', 'nap byen pase', 'nou anfom...']
    ws.reply(random.choice(repons))


@listen_to('joined')
def bienvenue(ws):
    mesajyo = ['Onè! Respè!', 'Bienvenue!', 'Welcome!']
    mesaj = random.choice(mesajyo)
    mesaj += '\n\nPlease add to your profile "What you do" (including the technologies you know).'
    mesaj += '\nAnd include your [city] right after your Display name (siw vle).'
    mesaj += '\nWe are happy you joined!'
    ws.reply(mesaj)


def main():
    Bot().run()


if __name__ == "__main__":
    main()
