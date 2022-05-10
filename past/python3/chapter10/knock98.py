import sys, numpy, math
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import ward, dendrogram

cvFile = numpy.load(sys.argv[1])
countryVectors = []
countryLabels = []
for k, v in zip(cvFile['header'], cvFile['data']):
    countryVectors.append(v)
    countryLabels.append(k)

wardVectors = ward(countryVectors)
dendrogram(wardVectors, labels=countryLabels)
plt.show()

