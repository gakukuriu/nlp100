#
# UNIXコマンドの場合 cut -f 1 filepath
# etc...
#

import sys

filepath = sys.argv[1]
col1 = sys.argv[2]
col2 = sys.argv[3]

with open(filepath) as f, open(col1, 'w') as c1, open(col2, 'w') as c2:
  for line in f:
    words = line.split('\t')
    c1.write(words[0] + '\n')
    c2.write(words[1] + '\n')

