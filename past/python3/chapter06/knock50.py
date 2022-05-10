import sys, re
    
with open(sys.argv[1], 'r') as rf:
    for line in rf:
        text = line
        while 1:
            result = re.search('[.;:?!] [A-Z]', text)
            if result == None:
                if text != '\n':
                    print(text, end='')
                break
            else:
                print(text[:result.start()+1])
                text = text[result.end()-1:]
            
