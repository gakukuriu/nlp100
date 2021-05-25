#
# 30.pyだとimportできないのでproblem30.pyとした
#

def loadMecab(filepath):
  neko = []
  sentence = []
  morpheme = {}
  flag = 1

  with open(filepath) as f:
    for l in f:
      if flag:
        if l == 'EOS\n':
          flag = 0
          neko.append(sentence)
          sentence = []
        else:
          l1 = l.split('\t')[0]
          l2 = l.split('\t')[1].split(',')
          morpheme['surface'] = l1
          morpheme['base'] = l2[6]
          morpheme['pos'] = l2[0]
          morpheme['pos1'] = l2[1]
          sentence.append(morpheme)
          morpheme = {}
      else:
        if l != 'EOS\n':
          flag = 1
          l1 = l.split('\t')[0]
          l2 = l.split('\t')[1].split(',')
          morpheme['surface'] = l1
          morpheme['base'] = l2[6]
          morpheme['pos'] = l2[0]
          morpheme['pos1'] = l2[1]
          sentence.append(morpheme)
          morpheme = {}                      

  return neko


