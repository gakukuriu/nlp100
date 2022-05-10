import sys

with open(sys.argv[1], 'r') as knock76Data:
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for line in knock76Data:
        ans = line.split('\t')[0][-2:]
        hyp = line.split('\t')[1][-2:]
        if ans == '+1':
            if hyp == '+1':
                TP += 1
            else:
                FN += 1
        else:
            if hyp == '+1':
                FP += 1
            else:
                TN += 1
    seikai = (TP + TN) / (TP + FP + FN + TN)
    tekigo = TP / (TP + FP)
    saigen = TP / (TP + FN)
    fvalue = (2 * tekigo * saigen) / (tekigo + saigen)
    print('正解率: '+str(seikai), '正例に関する適合率: '+str(tekigo), '再現率: '+str(saigen), 'F値: '+str(fvalue))
