import sys, json

neko = []
temp = []

with open(sys.argv[1], 'r') as rf, open(sys.argv[2], 'w') as wf:
    for line in rf:
        if line == 'EOS\n' and temp != []:
            neko.append(temp)
            temp = []
        elif line != 'EOS\n':
            tempdict = {}
            tempdict['surface'] = line.split('\t')[0]
            splits = line.split('\t')[1].split(',')
            tempdict['base'] = splits[-3]
            tempdict['pos'] = splits[0]
            tempdict['pos1'] = splits[1]
            temp.append(tempdict)
    json.dump(neko, wf)

for sentence in neko:
    for word in sentence:
        print(word)
    print()
