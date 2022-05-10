import sys, re
from collections import defaultdict

with open(sys.argv[1], 'r') as sent, open(sys.argv[2], 'w') as stop:
    sentDict = defaultdict(int)
    stopwordList = []
    for line in sent:
        temp = line.split(' ')
        for word in temp:
            sentDict[re.sub('[\.\,\;\:\!\?\(\)\"\']', '', word).strip()] += 1
    for item in sorted(sentDict.items(), key=lambda x:x[1], reverse=True)[:100]:
        stop.write(item[0]+'\n')
