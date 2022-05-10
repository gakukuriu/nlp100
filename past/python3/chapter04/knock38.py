import sys, json
import matplotlib.pyplot as plt
from collections import defaultdict

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    ansDict = defaultdict(int)
    for sentence in neko:
        for word in sentence:
            ansDict[word['surface']] += 1
    valueList = [v for k, v in ansDict.items()]
    plt.hist(valueList, range=(0, 50))
    plt.show()
