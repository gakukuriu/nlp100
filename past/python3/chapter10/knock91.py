import sys

with open(sys.argv[1], 'r') as qw, open(sys.argv[2], 'w') as familyF:
    switch = 0
    for line in qw:
        if line[:2] == ': ':
            if line == ': family\n':
                switch = 1
            elif switch == 1:
                switch = 0
        else:
            if switch == 1:
                familyF.write(line)
            
