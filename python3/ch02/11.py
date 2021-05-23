#
# UNIXコマンドの場合 cat filepath | tr '\t' ' '
# etc...
#

import sys

path = sys.argv[1]

with open(path) as f:
  for line in f:
    print(line.replace('\t', ' '), end='')
