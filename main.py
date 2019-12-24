#!/usr/bin/python

import click
from pprint import pprint
import funcs

import os



@click.command()
@click.option('--search')
@click.option('--count', default=5)

def temp(search, count):
    keywords = funcs.search(search, count)

    urls = []
    for item in keywords:
        print(str(item.get('index')) + ' - ' + item.get('title'))
        urls.append(item.get('video-url'))
        
    while True:
        sel = click.prompt('> ')

        if sel == 'exit':
            break
        else:
            try:
                sel = int(sel)
                os.system('mpv --really-quiet ' + urls[sel])
            except:
                print('Not a valid selection or mpv is having an issue.')
                
    
temp()