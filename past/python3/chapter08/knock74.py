import sys, json, numpy, knock71_function, learning

with open(sys.argv[1], 'r') as feature:
    weight = numpy.load(sys.argv[2])
    ids = json.load(feature)
    stopwordList = knock71_function.stopwordFunction(sys.argv[3])
    phi = learning.create_features(sys.argv[4], ids, stopwordList)
    h = learning.hypothesis(weight, phi)
    l = learning.sign(h, 0.5)
    if l == 1:
        l = '+1'
    else:
        l = str(l)
    print('Label: ' + l + '\t' + 'Probablity: ' + str(h))
