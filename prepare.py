#!/usr/bin/env python

import argparse
import requests

from pathlib import Path


session = requests.Session()
with open('cookie.txt') as f:
    cookie = f.read().strip()
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})

def get_input_data(day: int) -> list[str]:
  url = f'https://adventofcode.com/2023/day/{day}/input'
  text = session.get(url).text
  return [line.strip() for line in text.split("\n") if line.strip() != '']


parser = argparse.ArgumentParser("day.py")
parser.add_argument("day", help="AOC day to prepare", type=int)
args = parser.parse_args()

Path(f'day{args.day:02}').mkdir(exist_ok=True)

lines = get_input_data(args.day)
with open(f'day{args.day:02}/input.txt', 'w') as f:
    for line in lines:
        f.write(f"{line}\n")

