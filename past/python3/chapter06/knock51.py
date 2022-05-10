import sys, re
    
with open(sys.argv[1], 'r') as rf:
    for line in rf:
        for w in line.split(' '):
            print(re.sub('[,.]', '', w.strip()))
        print()
