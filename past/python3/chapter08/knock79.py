import sys, json, numpy, knock71_function, learning, matplotlib.pyplot as plt

def thresholdFunction(result, threshold):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for ans, prob in result:
        hyp = learning.sign(prob, threshold)
        if ans == 1:
            if hyp == 1:
                TP += 1
            else:
                FN += 1
        else:
            if hyp == 1:
                FP += 1
            else:
                TN += 1
    tekigo = TP / (TP + FP)
    saigen = TP / (TP + FN)
    return((tekigo, saigen))

with open(sys.argv[1], 'r') as sentiment, open(sys.argv[2], 'r') as feature:
    training_data = []
    for line in sentiment:
        training_data.append(line)
    division_data = [training_data[i:i+(int(len(training_data)/5))] for i in range(0, len(training_data), int(len(training_data)/5))]
    testData= division_data.pop(0)    
    trainData = [eel for el in division_data for eel in el]
    alpha = 1
    I = 10
    ids = json.load(feature)
    stopwordList = knock71_function.stopwordFunction(sys.argv[3])
    weight = numpy.zeros(len(ids))
    for i in range(I):
        for line in trainData:
            learning.learning(weight, ids, line, alpha, stopwordList)
    labels = []
    for line in testData:
        ans = int(line[:2])
        s = line[3:]
        phi = learning.create_features(s, ids, stopwordList)
        prob = learning.hypothesis(weight, phi)
        labels.append((ans, prob))
    tekigo_saigen = [(i, thresholdFunction(labels, (0.001 * i))) for i in range(1, 1000, 1)]
    print(tekigo_saigen)
#    plt.scatter(*zip(*tekigo_saigen))
#    plt.xlabel('適合率')
#    plt.ylabel('再現率')
#    plt.show()

