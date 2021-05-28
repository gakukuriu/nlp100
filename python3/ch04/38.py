import sys, problem30
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict


filepath = sys.argv[1]
neko = problem30.loadMecab(filepath)
d = defaultdict(int)

for s in neko:
  for w in s:
    d[w['surface']] += 1

freqList = list(map(lambda x: x[1], d.items()))
plt.hist(freqList)
plt.show()