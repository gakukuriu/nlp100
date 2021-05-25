import sys, problem30

filepath = sys.argv[1]
neko = problem30.loadMecab(filepath)

for s in neko:
  for w, i in zip(s, range(len(s))):
    if w['pos'] == '名詞' and (i+2) < len(s):
      if s[i+1]['surface'] == 'の' and s[i+2]['pos'] == '名詞':
        print(w['surface'] + s[i+1]['surface'] + s[i+2]['surface'])
