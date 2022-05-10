def stopwordFunction(stopwordFile):
    stopwordList = []
    with open(stopwordFile, 'r') as stop:
        for word in stop:
            stopwordList.append(word.strip())
    return(stopwordList)

def stopwordIn(keyword, stopwordFile):
    stopwordList = stopwordFunction(stopwordFile)
    return(keyword in stopwordList)

def test_stopwordIn():
    stopwordFile = '/Users/gkuriu/work/100knock_data/stopword.txt'
    print('--------- test ---------')
    print('"a" is stopword! is', stopwordIn('a', stopwordFile))
    print('"dope" is stopword! is', stopwordIn('dope', stopwordFile))
    print('------------------------')
