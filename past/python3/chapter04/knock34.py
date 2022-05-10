import sys, json

with open(sys.argv[1], 'r') as rf:
    neko = json.load(rf)
    for sentence in neko:
        for word in sentence:
            if word['surface'] == 'の':
                no_ind = sentence.index(word)
                try:
                    if no_ind > 0 and sentence[no_ind-1]['pos'] == '名詞' and sentence[no_ind+1]['pos'] == '名詞':
                        print(sentence[no_ind-1]['surface'], word['surface'], sentence[no_ind+1]['surface'])
                except IndexError:
                    pass
