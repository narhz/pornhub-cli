#!/usr/bin/python

import click
from pprint import pprint
import funcs

import os



@click.command()
@click.option('--search')
@click.option('--count', default=5)

def run(search, count):
    keywords = funcs.search(search, count)
    urls = []
    titles = []

    for item in keywords:
        titles.append(str(item.get('index')) + ' - ' + item.get('title'))
        urls.append(item.get('video-url'))

    funcs.disp(titles)
        
    while True:
        sel = click.prompt('> ')

        if sel == 'exit':
            break
        else:
            try:
                sel = int(sel)
                os.system('mpv --really-quiet ' + urls[sel])
                funcs.disp(titles)
            except:
                print('Not a valid selection or mpv is having an issue.')
                
    
run()