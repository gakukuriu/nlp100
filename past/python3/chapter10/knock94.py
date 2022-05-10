import sys, numpy, json, math
from gensim.models import word2vec

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    if denom != 0:
        return(numer / denom)
    else:
        return(0)
    
def similarity(model, ids, w1, w2, flag):
    if flag==1:
        return(model.similarity(w1, w2) * 10)
    else:
        return(cosSim(model[ids[w1]], model[ids[w2]]) * 10)

def addSim(model, ids, simList, writeF, flag):
    for line in simList:
        words = line.strip().split('\t')
        try:
            words.append(str(similarity(model, ids, words[0], words[1], flag)))
            writeF.write('\t'.join(words)+'\n')
        except KeyError:
            writeF.write('\t'.join(words)+'\n')

        
w2vModel = word2vec.Word2Vec.load(sys.argv[1])
myModel = numpy.load(sys.argv[2])
with open(sys.argv[3], 'r') as idFile, open(sys.argv[4], 'r') as simFile, open(sys.argv[5], 'w') as w2cAn, open(sys.argv[6], 'w') as myAn:
    ids = json.load(idFile)
    simList = []
    for line in simFile:
        simList.append(line)
    w2cAn.write(simList[0].strip()+'\tWord2Vec\n')
    myAn.write(simList[0].strip()+'\tMyVector\n')
    addSim(w2vModel, ids, simList[1:], w2cAn, 1)
    addSim(myModel, ids, simList[1:], myAn, 0)
