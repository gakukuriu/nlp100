import sys, re

filepath = sys.argv[1]
p = re.compile(r'\[?\[?(File:|ファイル:)([^\|]+)(.+)')

with open(filepath) as f:
  for s in f:
    m = p.match(s)
    if m:
      print(m[2])