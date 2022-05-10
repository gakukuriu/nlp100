import sys, json, numpy, knock71_function, learning

with open(sys.argv[1], 'r') as feature, open(sys.argv[4], 'r') as testdata:
    ids = json.load(feature)
    weight = numpy.load(sys.argv[2])
    stopwordList = knock71_function.stopwordFunction(sys.argv[3])
    for sentence in testdata:
        ans = sentence[:2]
        s = sentence[3:]
        phi = learning.create_features(s, ids, stopwordList)
        h = learning.hypothesis(weight, phi)
        l = learning.sign(h, 0.5)
        if l == 1:
            l = '+1'
        else:
            l = str(l)
        print('Answer: ' + ans + '\t' + 'Hypothesis: ' + l + '\t' + 'Probablity: ' + str(h))

