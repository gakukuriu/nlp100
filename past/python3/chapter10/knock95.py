import sys

def spearman(simList):
    human = {}
    vect = {}
    rank_human = {}
    sigmaD = 0
    for line in simList:
        sims = line.strip().split('\t')
        human['_'.join(sims[:2])] = float(sims[2])
        try:
            vect['_'.join(sims[:2])] = float(sims[3])
        except IndexError:
            vect['_'.join(sims[:2])] = -1
    i = 1
    for k, v in sorted(human.items(), key=lambda x:x[1], reverse=True):
        rank_human[k] = i
        i += 1
    j = 1
    N = 0
    for k, v in sorted(vect.items(), key=lambda x:x[1], reverse=True):
        if v != -1:
            sigmaD += (rank_human[k] - j) ** 2
            N += 1
        j += 1
    rho = 1 - ((6 * sigmaD) / ((N ** 3) - N))
    return(rho)
            

with open(sys.argv[1], 'r') as simF_w2v, open(sys.argv[2], 'r') as simF_myv:
    sim_w2v = []
    sim_myv = []
    for line in simF_w2v:
        sim_w2v.append(line)
    for line in simF_myv:
        sim_myv.append(line)
    print("Spearman's rank Correlation Coefficient of Word2Vec: ", str(spearman(sim_w2v[1:])))
    print("Spearman's rank Correlation Coefficient of My Vector: ", str(spearman(sim_myv[1:])))
    
