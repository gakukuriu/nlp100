#
# UNIXコマンドの場合 head -n filepath
#

import sys

filepath = sys.argv[1]
n = int(sys.argv[2])

with open(filepath) as f:
  lines = f.readlines()
  for l in lines[:n]:
    print(l, end='')