#
# UNIXコマンドの場合 splitにN分割オプションがなかった
# usage: split [-a sufflen] [-b byte_count] [-l line_count] [-p pattern]
#              [file [prefix]]
# ので、n行単位での分割を以下でも行った
# n行単位での分割はUNIXコマンドでは split -l n filepath
#

import sys

n = int(sys.argv[1])
filepath = sys.argv[2]
filename = sys.argv[3]

with open(filepath) as f:
  lines = f.readlines()
  if (len(lines) % n) != 0:
    fileNumber = (len(lines) // n) + 1
  else:
    fileNumber = len(lines) // n
  for i in range(fileNumber):
    with open(filename + str(i) + '.txt', 'w') as g:
      for l in lines[(n*i):(n*(i+1))]:
        g.write(l)