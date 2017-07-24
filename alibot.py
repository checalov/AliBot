import requests
import urllib.parse
import json
import random

from errbot import BotPlugin, botcmd

ASCII_API = 'http://artii.herokuapp.com/make'
QUOTES = 'http://loremricksum.com/api/?paragraphs=1&quotes=1'
random.seed()

# Other font are here
# http://artii.herokuapp.com/fonts_list
FONTS = [
    'kban',
    'letters',
    'madrid',
    'lean',
    'fender',
    'doom',
    'cybermedium',
    'cosmike',
    'colossal',
    'caligraphy',
    'big'
]


def dict2querystring(d):
    return '&'.join(['='.join([str(k), str(v)]) for k, v in d.items()])


def get_quote():
    data = requests.get(QUOTES).json()
    return data['data'][0]


def wrap(text, chars_inline=10):
    last_stop = 0
    for i in range(chars_inline, len(text), chars_inline):
        e = last_stop + chars_inline
        while e < len(text) and text[e] != ' ':
            e += 1

        yield text[last_stop:e]
        last_stop = last_stop + e - last_stop + 1
        if e >= len(text):
            return


class Help(BotPlugin):
    @botcmd
    def quote(self, msg, args):
        quote = get_quote()
        # font = random.choice(FONTS)

        # for lin in wrap(quote):
        #     ascii = requests.get(ASCII_API, {'font': font,
        #                                      'text': urllib.parse.quote_plus(lin)}).text
        #     yield ascii

        return quote
