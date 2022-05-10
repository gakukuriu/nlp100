import sys, numpy, math
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

cvFile = numpy.load(sys.argv[1])
countryVectors = []
for k, v in zip(cvFile['header'], cvFile['data']):
    countryVectors.append(v)

model = TSNE()
tsneVectors = model.fit_transform(countryVectors)
x = tsneVectors[:, 0]
y = tsneVectors[:, 1]
plt.scatter(x, y)
plt.title('t-SNE')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
