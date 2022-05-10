import sys, json
import matplotlib.pyplot as plt
from collections import defaultdict

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    ansDict = defaultdict(int)
    for sentence in neko:
        for word in sentence:
            ansDict[word['surface']] += 1
    top10 = sorted(ansDict.items(), key = lambda x:x[1], reverse=True)
    keylist = [k for k, v in top10][:10]
    valuelist = [v for k, v in top10][:10]
    x = [i for i in range(10)]
    plt.bar(x, valuelist, align = 'center')
    plt.title('頻度上位10単語')
    plt.xlabel('語句')
    plt.ylabel('頻度')
    plt.xticks(x, keylist)
    plt.show()

