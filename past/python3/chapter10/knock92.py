import sys, numpy, json, math
from gensim.models import word2vec

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    return(numer / denom)

def mostSimilar(model, ids, vec, flag):
    if flag==1:
        result = model.most_similar(positive=[vec])
        return(result[0])
    else:
        simDict = {}
        for k, v in ids.items():
            sim = cosSim(vec, model[v])
            if not(numpy.isnan(sim)):
                simDict[k] = sim
        return(sorted(simDict.items(), key=lambda x:x[1], reverse=True)[0])
                
def analogyEval(model, ids, analogyF, writeF, flag):
    for line in analogyF:
        try:
            words = line.strip().split(' ')
            if flag==1:
                vec = model[words[1]] - model[words[0]] + model[words[2]]
            else:
                vec = model[ids[words[1]]] - model[ids[words[0]]] + model[ids[words[2]]]
            try:
                w, s = mostSimilar(model, ids, vec, flag)
                words += [w, str(s)]
                writeF.write(' '.join(words)+'\n')
            except IndexError:
                print('index error.')
        except KeyError:
            print('key is not found.')


w2vModel = word2vec.Word2Vec.load(sys.argv[1])
myModel = numpy.load(sys.argv[2])
with open(sys.argv[3], 'r') as idFile, open(sys.argv[4], 'r') as analogyF, open(sys.argv[5], 'w') as w2cAn, open(sys.argv[6], 'w') as myAn:
    ids = json.load(idFile)
    analogies = []
    for line in analogyF:
        analogies.append(line)
    analogyEval(w2vModel, ids, analogies, w2cAn, 1)
    analogyEval(myModel, ids, analogies, myAn, 0)

        
