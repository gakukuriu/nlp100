import sys, json, numpy, knock71_function, learning
    
with open(sys.argv[1], 'r') as learningData, open(sys.argv[2], 'r') as feature:
    ids = json.load(feature)
    alpha = 1
    I = 10
    weight = numpy.zeros(len(ids))
    stopwordList = knock71_function.stopwordFunction(sys.argv[3])
    training_data = []
    for line in learningData:
        training_data.append(line)
    for i in range(I):
        for line in training_data:
            learning.learning(weight, ids, line, alpha, stopwordList)
    numpy.save(sys.argv[4], weight)

    
    
