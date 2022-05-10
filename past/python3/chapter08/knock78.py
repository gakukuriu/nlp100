import sys, json, numpy, knock71_function, learning

with open(sys.argv[1], 'r') as sentiment, open(sys.argv[2], 'r') as feature:
    training_data = []
    for line in sentiment:
        training_data.append(line)
    division_data = [training_data[i:i+(int(len(training_data)/5))] for i in range(0, len(training_data), int(len(training_data)/5))]
    ids = json.load(feature)
    alpha = 1
    I = 10
    stopwordList = knock71_function.stopwordFunction(sys.argv[3])
    seikai = 0
    tekigo = 0
    saigen = 0
    fvalue = 0
    for i in range(5):
        temp = division_data[:]
        testData = temp.pop(i)
        trainData = [eel for el in temp for eel in el]
        weight = numpy.zeros(len(ids))
        for line in trainData:
            learning.learning(weight, ids, line, alpha, stopwordList)
        labels = []
        for line in testData:
            ans = line[:2]
            s = line[3:]
            phi = learning.create_features(s, ids, stopwordList)
            hyp = learning.sign(learning.hypothesis(weight, phi), 0.5)
            labels.append((int(ans), hyp))
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for ans, hyp in labels:
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
        seikai_temp = (TP + TN) / (TP + FP + FN + TN)
        tekigo_temp = TP / (TP + FP)
        saigen_temp = TP / (TP + FN)
        fvalue_temp = (2 * tekigo_temp * saigen_temp) / (tekigo_temp + saigen_temp)
        print('---------'+'実験'+str(i+1)+'----------')
        print('正解率: '+str(seikai_temp), '正例に関する適合率: '+str(tekigo_temp), '再現率: '+str(saigen_temp), 'F値: '+str(fvalue_temp))
        seikai += seikai_temp
        tekigo += tekigo_temp
        saigen += saigen_temp
        fvalue += fvalue_temp

    seikai = seikai / 5
    tekigo = tekigo / 5
    saigen = saigen / 5
    fvalue = fvalue / 5
    print('---------最終結果---------')
    print('正解率: '+str(seikai), '正例に関する適合率: '+str(tekigo), '再現率: '+str(saigen), 'F値: '+str(fvalue))

            

        
