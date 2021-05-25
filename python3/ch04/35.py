import sys, problem30

filepath = sys.argv[1]
neko = problem30.loadMecab(filepath)

for s in neko:
  flag = 0
  nouns = []
  for w in s:
    if flag:
      if w['pos'] == '名詞':
        nouns.append(w['surface'])
      else:
        if len(nouns) > 1:
          print(' '.join(nouns))
          nouns = []
        else:
          nouns = []
    else:
      if w['pos'] == '名詞':
        flag = 1
        nouns.append(w['surface'])
  if len(nouns) > 1:
    print(' '.join(nouns))