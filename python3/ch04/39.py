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

x = list(range(1, len(d.items()) + 1))
y = list(map(lambda x: x[1], sorted(d.items(), key=lambda x: x[1], reverse=True)))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('単語の出現頻度順位')
ax.set_ylabel('出現頻度')
ax.set_title('Zipfの法則')
plt.show()