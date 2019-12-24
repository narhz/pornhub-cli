#!/usr/bin/python

import click
from pprint import pprint
import funcs

@click.command()
@click.option('--search')
@click.option('--count', default=5)

def temp(search, count):
    keywords = funcs.search(search, count)

    for item in keywords:
        print(str(item.get('index')) + ' - ' + item.get('title'))


temp()