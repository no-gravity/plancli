#!/usr/bin/python3 -B

import re
import datetime
from textwrap import dedent

def main():
    title = ''
    while not title:
        title = input('Title: ').lower()
        title = re.sub('[^a-z0-9-]', '_', title)
    info = input('Info: ')
    eta = ''
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    while not re.match(r'^(\d+h\d+m?|\d+h|\d+m)$', eta):
        eta = input('ETA: ')
    priority = ''
    while not re.match(r'^\d+$', priority):
        priority = input('Priority: ')
    out = dedent(f"""\
        created: {now}
        eta: {eta}
        elapsed:
        info:

            {info}
    """)
    file = f"{priority}-{title}.txt"
    with open(file, 'w') as f: f.write(out)

main()
