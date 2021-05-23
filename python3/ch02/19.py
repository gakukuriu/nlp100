#
# UNIXコマンドの場合 cut -f 1 filepath | sort | uniq -c | sort -nr
#

import sys
from collections import defaultdict

filepath = sys.argv[1]
d = defaultdict(int)

with open(filepath) as f:
  for line in f:
    d[line.split('\t')[0]] += 1
  for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
