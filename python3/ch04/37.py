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

left = list(range(1,11))
right = []
labels = []
for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)[:10]:
  labels.append(k)
  right.append(v)

plt.bar(left, right, tick_label=labels)
plt.show()