import sys, re
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
sentenceList = []

for sentences in root.iter('sentences'):
    for sentence in sentences.findall('sentence'):
        temp = []
        for tokens in sentence.findall('tokens'):
            for token in tokens.findall('token'):
                temp.append(token.find('word').text)
        sentenceList.append(temp)

for coreference in root.iter('coreference'):
    for mention in coreference.findall('mention'):
        if mention.get('representative') == 'true':
            rep = mention.find('text').text
        else:
            sentence = int(mention.find('sentence').text)-1
            start = int(mention.find('start').text)-1
            end = int(mention.find('end').text)-1
            templist = sentenceList[:]
            temp = templist[sentence][:start] + [rep + '(' + mention.find('text').text + ')'] + templist[sentence][end:]
            sentenceList[sentence] = temp

for s in sentenceList:
    for w in s:
        print(w, end=' ')
    print()
