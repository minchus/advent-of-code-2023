#!/usr/bin/env python

import argparse
import requests

from pathlib import Path
from os.path import join


session = requests.Session()
with open('cookie.txt') as f:
    cookie = f.read().strip()
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})

def get_input_data(day: int) -> str:
  url = f'https://adventofcode.com/2023/day/{day}/input'
  text = session.get(url).text
  return text


parser = argparse.ArgumentParser("day.py")
parser.add_argument("day", help="AOC day to prepare", type=int)
args = parser.parse_args()

day_number = args.day
new_dir = f'day{day_number:02}'
Path(new_dir).mkdir(exist_ok=True)
Path(join(new_dir, 'main.py')).touch()

text = get_input_data(args.day)
with open(join(new_dir, 'input.txt'), 'w') as f:
        f.write(text)

