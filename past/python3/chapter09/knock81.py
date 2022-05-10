import sys, re

with open(sys.argv[1], 'r') as corpus, open(sys.argv[2], 'r') as countries, open(sys.argv[3], 'w') as newCorpus:
    countryList = []
    for c in countries:
        countryList.append(c.split('|')[1].strip())

    for t in corpus:
        temp = t
        for c in countryList:
            temp = re.sub(c, c.replace(' ', '_'), temp, flags=re.IGNORECASE)
        newCorpus.write(temp)
