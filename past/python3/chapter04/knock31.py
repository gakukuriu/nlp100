import sys, json

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    for sentence in neko:
        for word in sentence:
            if word['pos'] == '動詞':
                print(word['surface'])
