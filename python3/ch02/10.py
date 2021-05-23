#
# UNIXコマンドの場合 wc -l
#

import sys

path = sys.argv[1]

with open(path) as f:
  length = 0
  for _ in f:
    length += 1
  print(length)