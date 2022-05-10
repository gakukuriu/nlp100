import sys, json, math, numpy
from collections import defaultdict
from scipy import io, sparse

with open(sys.argv[1], 'r') as ftc, open(sys.argv[2], 'r') as ftall, open(sys.argv[3], 'r') as fallc, open(sys.argv[4], 'w') as rowIdFile, open(sys.argv[5], 'w') as columnIdFile:
    f_t_c = json.load(ftc)
    f_t_all = json.load(ftall)
    f_all_c = json.load(fallc)
    N = 68021243
    
    rowIds = defaultdict(lambda: len(rowIds))
    columnIds = defaultdict(lambda: len(columnIds))
    for k, v in f_t_all.items():
        temp = rowIds[k]
    for k, v in f_all_c.items():
        temp = columnIds[k]

    A = sparse.lil_matrix((len(f_t_all), len(f_all_c)))
    for k, v in f_t_c.items():
        if v >= 10:
            t = k.split('\t')[0]
            c = k.split('\t')[1]
            ansCand = math.log((N * v) / (f_t_all[t] * f_all_c[c]))
            i = rowIds[t]
            j = columnIds[c]
            A[i, j] = max(ansCand, 0)
    
    json.dump(dict(rowIds), rowIdFile)
    json.dump(dict(columnIds), columnIdFile)
    io.savemat(sys.argv[6], {'A':A})
    
