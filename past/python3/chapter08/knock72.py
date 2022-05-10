import sys, re, json, knock71_function
from stemming.porter2 import stem
from collections import defaultdict

with open(sys.argv[1], 'r') as sent, open(sys.argv[3], 'w') as feature:
    stopwordList = knock71_function.stopwordFunction(sys.argv[2])
    ids = defaultdict(lambda: len(ids))
    featureDict = {}
    for line in sent:
        templist = line.split(' ')
        for word in templist:
            tempword = re.sub('[\.\,\;\:\!\?\(\)\"\']', '', word).strip()
            if not(tempword in stopwordList):
                featureDict[ids[stem(tempword)]] = 0
    json.dump(ids, feature)
