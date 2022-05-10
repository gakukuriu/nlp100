import sys, json

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

with open(sys.argv[1], 'r') as rf:
    templist = []
    anslist = []
    for line in rf:
        if line != 'EOS\n':
            if line[:2] != '* ':
                f_s = line.split('\t')
                s_s = f_s[1].split(',')
                templist.append(Morph(f_s[0], s_s[-3], s_s[0], s_s[1]))
        elif templist != []:
            anslist.append(templist)
            templist = []
    for word in anslist[2]:
        print(word.surface, end=' ')
    print()
        
        
