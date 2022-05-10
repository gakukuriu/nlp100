import sys
from stemming.porter2 import stem

with open(sys.argv[1], 'r') as rf:
    for line in rf:
        word = line.strip()
        print(word+'\t'+stem(word))
