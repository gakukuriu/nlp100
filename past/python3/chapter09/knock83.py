import sys, json
from collections import defaultdict


with open(sys.argv[1], 'r') as context, open(sys.argv[2], 'w') as ftc, open(sys.argv[3], 'w') as ftall, open(sys.argv[4], 'w') as fallc:
    f_t_c = defaultdict(int)
    f_t_all = defaultdict(int)
    f_all_c = defaultdict(int)
    N = 0

    for line in context:
        t = line.split('\t')[0]
        cs = json.loads(line.split('\t')[1].strip())
        f_t_all[t] += 1
        for c in cs:
            N += 1
            f_all_c[c] += 1
            f_t_c[t+'\t'+c] += 1

    json.dump(dict(f_t_c), ftc)
    json.dump(dict(f_t_all), ftall)
    json.dump(dict(f_all_c), fallc)
    print(N)
