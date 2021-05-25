import sys, problem30
from collections import defaultdict


filepath = sys.argv[1]
neko = problem30.loadMecab(filepath)
d = defaultdict(int)

for s in neko:
  for w in s:
    d[w['surface']] += 1

for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
  print(k, v)