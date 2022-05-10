import sys, json, random

def surround(s, i, d):
    if i-d < 0:
        start = 0
    else:
        start = i-d
    end = i+d+1
    ans = s[start:i] + s[i+1:end]
    return(ans)

with open(sys.argv[1] ,'r') as corpus, open(sys.argv[2], 'w') as context:
    for line in corpus:
        words = line.strip().split(' ')
        for i in range(len(words)):
            t = random.randint(1, 5)
            context.write(words[i]+'\t'+json.dumps(surround(words, i, t))+'\n')
