import sys, json

def printList(lst):
    for el in lst:
        print(el+' ', end='')
    print()
    
with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    for sentence in neko:
        temppos = []
        apStart = -1
        apEnd = -1
        for word in sentence:
            if word['pos'] == '名詞' and apStart == -1:
                apStart = sentence.index(word)
                apEnd = sentence.index(word)
                temppos.append(word['surface'])
            elif word['pos'] == '名詞' and apStart != -1:
                apEnd = sentence.index(word)
                temppos.append(word['surface'])
            elif word['pos'] != '名詞' and (apEnd - apStart) > 1 and apStart != -1:
                printList(temppos)
                temppos = []
                apStart = -1
                apEnd = -1
            else:
                temppos = []
                apStart = -1
                apEnd = -1
