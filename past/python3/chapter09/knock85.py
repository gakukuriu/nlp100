import sys, numpy
from sklearn.decomposition import RandomizedPCA
from scipy import io
from scipy.sparse.linalg import svds

w_c_a = (io.loadmat(sys.argv[1])['A']).tocsr()
U, S, V = svds(w_c_a, 300)
numpy.save(sys.argv[2], U * S)

    
