import sys, re

filepath = sys.argv[1]
p = re.compile(r'(\=+)([^\=]+)(\=+)')

with open(filepath) as f:
  for s in f:
    m = p.match(s)
    if m:
      level = str(len(m[1].strip()) - 1)
      print('Section Name: ' + m[2] + ' Level: ' + level)