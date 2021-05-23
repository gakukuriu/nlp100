#
# UNIXコマンドの場合 cut -f 1 filepath | sort -u
#

import sys

filepath = sys.argv[1]

with open(filepath) as f:
  col1 = []
  for line in f:
    col1.append(line.split('\t')[0])
  col1Set = set(col1)
  print(col1Set) 