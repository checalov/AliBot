#!/usr/bin/python3
import urllib.request
import urllib.parse
import json
import random


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


def GET(url, query=None):
  if query:
    query_string = dict2querystring(query)
    url += '?' + query_string
    
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as response:
    return response.read().decode('utf-8')
  
def get_quote():
  data = json.loads(GET(QUOTES))
  return data['data'][0]
  
  
def wrap(text, chars_inline=10):
  last_stop = 0
  for i in range(chars_inline, len(text), chars_inline):
    e = last_stop+chars_inline
    while e < len(text) and text[e] != ' ':
      e += 1
      
    yield text[last_stop:e]
    last_stop = last_stop + e - last_stop + 1
    if e >= len(text):
      return
    
  
def main(*args):
  quote = get_quote()
  font = random.choice(FONTS)
  
  for lin in wrap(quote):
    ascii = GET(ASCII_API, {'font': font, 'text': urllib.parse.quote_plus(lin)})
    print(ascii)
  
  
if __name__ == '__main__':
  main()
