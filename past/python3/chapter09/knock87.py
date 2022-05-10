import sys, numpy, json, math

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    return(numer / denom)

with open(sys.argv[1], 'r') as idFile:
    semanticArray = numpy.load(sys.argv[2])
    ids = json.load(idFile)
    v1 = semanticArray[ids['United_States']]
    v2 = semanticArray[ids['U.S']]
    print(cosSim(v1, v2))
