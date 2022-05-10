import sys, numpy
from gensim.models import word2vec

w2vModel = word2vec.Word2Vec.load(sys.argv[1])
with open(sys.argv[2], 'r') as countries, open(sys.argv[3], 'w') as countryVectorFile:
    countryList = []
    countryVectors = {}
    for c in countries:
        countryList.append((c.split('|')[1].strip()).replace(' ', '_'))

    for c in countryList:
        try:
            countryVectors[c] = w2vModel[c]
        except KeyError:
            pass
    cvList = list(countryVectors.items())
    numpy.savez(sys.argv[3], header=[k for k, v in cvList], data=[v for k, v in cvList])

