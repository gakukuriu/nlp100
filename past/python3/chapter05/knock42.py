import sys, json

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        
class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

def sentence_to_chunk(sentence):
    ansSentence = []
    for i in range(len(sentence)):
        temp = Chunk()
        temp.morphs = sentence[i][1:]
        temp.dst = sentence[i][0]
        ansSentence.append(temp)
    for i in range(len(sentence)):
        if sentence[i][0] > -1:
            ansSentence[sentence[i][0]].srcs.append(i)
    return(ansSentence)

def morphsPrint(morphs):
    for w in morphs:
        if w.pos != '記号':
            print(w.surface, end='')
        
with open(sys.argv[1], 'r') as rf:
    switch = 0
    morphlist = []
    sentence = []
    templist = []
    for line in rf:
        if line != 'EOS\n':
            if line[:2] != '* ':
                f_s = line.split('\t')
                s_s = f_s[1].split(',')
                morphlist.append(Morph(f_s[0], s_s[-3], s_s[0], s_s[1]))
            elif switch == 0:
                morphlist.append(int(line.split(' ')[2][:-1]))
                switch = 1
            else:
                sentence.append(morphlist)
                morphlist = [int(line.split(' ')[2][:-1])]
        elif sentence != [] or (morphlist != [] and switch == 1):
            sentence.append(morphlist)
            templist.append(sentence)
            morphlist = []
            sentence = []
            switch = 0
    anslist = list(map(sentence_to_chunk, templist))

    for s in anslist:
        for chk in s:
            if chk.dst != -1:
                morphsPrint(chk.morphs)
                print('\t', end='')
                morphsPrint(s[chk.dst].morphs)
                print()        
