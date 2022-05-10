import sys, numpy, json, math

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    return(numer / denom)

with open(sys.argv[1], 'r') as idFile:
    semanticArray = numpy.load(sys.argv[2])
    ids = json.load(idFile)
    simDict = {}
    spainVec = semanticArray[ids['England']]
    madridVec = semanticArray[ids['Madrid']]
    athensVec = semanticArray[ids['Athens']]
    vec = spainVec - madridVec + athensVec

    for k, v in ids.items():
        sim = cosSim(vec, semanticArray[v])
        if not(numpy.isnan(sim)):
            simDict[k] = sim

    for k, v in sorted(simDict.items(), key=lambda x:x[1], reverse=True)[:10]:
        print(k, v)
