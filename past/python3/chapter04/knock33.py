import sys, json

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    for sentence in neko:
        for word in sentence:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                print(word['surface'])
