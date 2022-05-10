# UNIXコマンド:
## cut -f1  ~/work/100knock_data/knock47_data.txt | sort | uniq -c | sort -r | head
## sort ~/work/100knock_data/knock47_data.txt | uniq -c | sort -r | head

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

def inPhrase(chk, p):
    for w in chk.morphs:
        if w.pos == p:
            return True
    return False

def knk47InPhrase(chk, p1, p2, sur):
    for i in range(len(chk.morphs)-1):
        if chk.morphs[i+1].pos == p2 and chk.morphs[i+1].surface == sur and chk.morphs[i].pos1 == p1:
            return True
    return False

def knk47Return(chk, p1, p2, sur):
    answer = ''
    for w in chk.morphs:
        if w.pos1 == p1:
            answer += w.surface
        elif w.pos == p2 and w.surface == sur:
            answer += w.surface
    return(answer)

def mostleftBaseReturn(chk, p):
    for w in chk.morphs:
        if w.pos == p:
            return(w.base)

def mostrightSurfaceReturn(chk, p):
    temp = []
    for w in chk.morphs:
        if w.pos == p:
            temp.append(w.surface)
    return(temp[-1])

def surfaceReturn(chk, p):
    answer = ''
    for w in chk.morphs:
        if w.pos == p:
            answer += w.surface + ','
    return(answer[:-1])

def chkReturn(chk):
    answer = ''
    for w in chk.morphs:
        answer += w.surface
    return(answer)

    
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
            verb = ''
            bphrase = ''
            pp = ''
            term = ''
            if inPhrase(chk, '動詞'):
                verb += mostleftBaseReturn(chk, '動詞') + '\t'
                for n in chk.srcs:
                    if knk47InPhrase(s[n], 'サ変接続', '助詞', 'を'):
                        bphrase += knk47Return(s[n], 'サ変接続', '助詞', 'を')
                    elif inPhrase(s[n], '助詞'):
                        pp += mostrightSurfaceReturn(s[n], '助詞') + ' '
                        term += chkReturn(s[n]) + ' '
                if bphrase != '' and pp != '':
                    print(bphrase + verb + pp.strip() + '\t' + term.strip())
