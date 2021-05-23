#
# UNIXコマンドの場合 paste col1.txt col2.txt
#

import sys

col1 = sys.argv[1]
col2 = sys.argv[2]
col1_2 = sys.argv[3]

with open(col1) as c1, open(col2) as c2, open(col1_2, 'w') as c1_2:
  c1Line = c1.readline()
  c2Line = c2.readline()
  while c1Line:
    c1_2.write(c1Line[:-1] + '\t' + c2Line)
    c1Line = c1.readline()
    c2Line = c2.readline()