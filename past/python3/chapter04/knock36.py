import sys, json
from collections import defaultdict

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    ansDict = defaultdict(int)
    for sentence in neko:
        for word in sentence:
            ansDict[word['surface']] += 1
    for k, v in sorted(ansDict.items(), key = lambda x:x[1], reverse=True):
        print(k+'\t'+str(v))
    
