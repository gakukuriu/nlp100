import sys, json
import matplotlib.pyplot as plt
from collections import defaultdict

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    ansDict = defaultdict(int)
    for sentence in neko:
        for word in sentence:
            ansDict[word['surface']] += 1
    sortList = sorted(ansDict.items(), key = lambda x:x[1], reverse=True)
    rankList = [i+1 for i in range(len(sortList))]
    valueList = [v for k, v in sortList]
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Zipfの法則')
    plt.xlabel('出現頻度順位(log)')
    plt.ylabel('出現頻度(log)')
    plt.plot(rankList, valueList)
    plt.show()


