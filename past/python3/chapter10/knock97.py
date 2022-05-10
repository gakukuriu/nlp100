import sys, numpy, math

def cosSim(v1, v2):
    numer = numpy.dot(v1, v2)
    denom = math.sqrt(numpy.dot(v1, v1)) * math.sqrt(numpy.dot(v2, v2))
    return(numer / denom)

def initialSeparate(data, kNum):
    anslist = []
    elemNum = len(data) // kNum
    init = (len(data) % kNum) + elemNum
    anslist.append(data[:init])
    anslist += [data[i:i+elemNum] for i in range(init, len(data), elemNum)]
    return(anslist)

def meanFunc(data):
    ans = 0
    for k, v in data:
        ans += v
    return(ans / len(data))

def kmeans(data, separatedlist, kNum):
    means = list(map(lambda l: meanFunc(l), separatedlist))
    anslist = [[] for i in range(kNum)]
    for k, v in data:
        bestk = 0
        bestSim = cosSim(v, means[0])
        for i in range(1, len(means)):
            temp = cosSim(v, means[i])
            if bestSim < temp:
                bestSim = temp
                bestk = i
        anslist[bestk] += [(k, v)]
    if separatedlist == anslist:
        return(anslist)
    else:
        return(kmeans(data, anslist, kNum))
    
    
cvFile = numpy.load(sys.argv[1])
countryVectors = []
for k, v in zip(cvFile['header'], cvFile['data']):
    countryVectors.append((k, v))
kNumber = 5
initialVectors = initialSeparate(countryVectors, kNumber)
ans = kmeans(countryVectors, initialVectors, kNumber)

for i in range(len(ans)):
    print('--------- Cluster'+str(i+1)+' ---------')
    for k, v in ans[i]:
        print(' '+k, end='')
    print()
    
    
