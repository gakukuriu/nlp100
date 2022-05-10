import sys, numpy, json, math, logging
from gensim.models import word2vec

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    return(numer / denom)

def knock86(model):
    print(model['United_States'])

def knock87(model):
    v1 = model['United_States']
    v2 = model['U.S']
    print(cosSim(v1, v2))

def knock88(model, ids):
    simDict = {}
    englandVec = model['England']
    for k, v in ids.items():
        if k != 'England' and k in model:
            sim = cosSim(englandVec, model[k])
            if not(numpy.isnan(sim)):
                simDict[k] = sim
    for k, v in sorted(simDict.items(), key=lambda x:x[1], reverse=True)[:10]:
        print(k, v)

def knock89(model, ids):
    simDict = {}
    spainVec = model['England']
    madridVec = model['Madrid']
    athensVec = model['Athens']
    vec = spainVec - madridVec + athensVec
    for k, v in ids.items():
        if k in model:
            sim = cosSim(vec, model[k])
            if not(numpy.isnan(sim)):
                simDict[k] = sim
    for k, v in sorted(simDict.items(), key=lambda x:x[1], reverse=True)[:10]:
        print(k, v)

        
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data = word2vec.Text8Corpus(sys.argv[1])
model = word2vec.Word2Vec(data, size=300)
model.save(sys.argv[3])


with open(sys.argv[2], 'r') as idFile:
    ids = json.load(idFile)

    print('--------- knock86 ---------')
    knock86(model)
    print()

    print('--------- knock87 ---------')
    knock87(model)
    print()

    print('--------- knock88 ---------')
    knock88(model, ids)
    print()

    print('--------- knock89 ---------')
    knock89(model, ids)
