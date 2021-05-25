import sys, problem30

filepath = sys.argv[1]
neko = problem30.loadMecab(filepath)

for s in neko:
  for w in s:
    if w['pos1'] == 'サ変接続':
      print(w)