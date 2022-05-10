import sys, re

with open(sys.argv[1], 'r') as protoCorpus, open(sys.argv[2], 'w') as corpus:
    for line in protoCorpus:
        tokens = line.split(' ')
        tokens = list(map(lambda s: s.strip('.,!?;:()[]\'\"\n'), tokens))
        tokens = list(filter(lambda s: s != '', tokens))
        if tokens != []:
            corpus.write(' '.join(tokens) + '\n')
        
