import sys, re

filepath = sys.argv[1]
p = re.compile(r'\[\[Category:')

with open(filepath) as f:
  for s in f:
    if p.match(s):
      print(s, end='')