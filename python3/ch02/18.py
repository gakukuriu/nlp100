#
# UNIXコマンドの場合 sort -r -k 3 filepath
#

import sys

filepath = sys.argv[1]

with open(filepath) as f:
  splitLines = map(lambda l: l.split('\t'), f.readlines())
  for l in sorted(splitLines, key=lambda x: x[2], reverse=True):
    print('\t'.join(l), end='')
