import sys, numpy, json

with open(sys.argv[1], 'r') as idFile:
    semanticArray = numpy.load(sys.argv[2])
    ids = json.load(idFile)
    print(semanticArray[ids['United_States']])
