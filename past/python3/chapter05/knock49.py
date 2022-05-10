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

def chkReturn(chk):
    answer = ''
    for w in chk.morphs:
        answer += w.surface
    return(answer)

def chkSubstReturn(chk, p, sb):
    answer = ''
    switch = 0
    for w in chk.morphs:
        if w.pos == p and switch == 0:
            answer += sb
            switch = 1
        else:
            answer += w.surface
    return(answer)

def havePath(s, n1, n2):
    if s[n1].dst == n2:
        return(True)
    elif s[n1].dst == -1:
        if s[n2].dst == -1:
            return(True)
        else:
            return(False)
    else:
        return(havePath(s, s[n1].dst, n2))

def pathToNum(s, n1, n2):
    if n1 == n2:
        return(chkReturn(s[n2]))
    elif s[n1].dst == n2:
        return(chkReturn(s[n1]) + ' -> ' + chkReturn(s[n2]))
    else:
        return(chkReturn(s[n1]) + ' -> ' + pathToNum(s, s[n1].dst, n2))

def pathToNumWithOption(s, n1, n2, p, sb):
    if n1 == n2:
        return(chkSubstReturn(s[n2], p, sb))
    elif s[n1].dst == n2:
        return(chkReturn(s[n1]) + ' -> ' + chkSubstReturn(s[n2], p, sb))
    else:
        return(chkReturn(s[n1]) + ' -> ' + pathToNumWithOption(s, s[n1].dst, n2, p, sb))
    
def knock49PathToNum(s, n1, n2, opt, p1, sb1, p2, sb2):
    if n1 == n2:
        return(chkSubstReturn(s[n1], p1, sb1))
    elif opt == 1:
        return(chkSubstReturn(s[n1], p1, sb1) + ' -> ' + pathToNumWithOption(s, s[n1].dst, n2, p2, sb2))
    else:
        return(chkSubstReturn(s[n1], p1, sb1) + ' -> ' + pathToNum(s, s[n1].dst, n2))

def pathListFunction(s, n):
    if s[n].dst == -1:
        return([n])
    else:
        return([n] + pathListFunction(s, s[n].dst))

def pathListCommons(l1, l2):
    templist = []
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                templist.append(e1)
    return(templist[0])

def pathListCommonBefore(l, n):
    templist = []
    for e in l:
        if e == n:
            if templist == []:
                return(n)
            else:
                return(templist[-1])
        else:
            templist.append(e)


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
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if inPhrase(s[i], '名詞') and inPhrase(s[j], '名詞'):
                    if havePath(s, i, j):
                        print(knock49PathToNum(s, i, j, 1, '名詞', 'X', '名詞', 'Y'))
                    else:
                        ilist = pathListFunction(s, i)
                        jlist = pathListFunction(s, j)
                        commonNum = pathListCommons(ilist, jlist)
                        endi = pathListCommonBefore(ilist, commonNum)
                        endj = pathListCommonBefore(jlist, commonNum)
                        print(knock49PathToNum(s, i, endi, 0, '名詞', 'X', '', '') + ' | ' + knock49PathToNum(s, j, endj, 0, '名詞', 'Y', '', '') + ' | ' + chkReturn(s[commonNum]))
