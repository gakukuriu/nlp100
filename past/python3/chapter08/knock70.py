# nkfを使ってrt-polarity.posの文字コードをutf-8に変換しておく(negについても同様)
## nkf -w rt-polarity.pos > u_rt-polarity.pos
# 正例・負例の数の確認
## cut -d' ' -f 1 ~/work/100knock_data/hightemp.txt | sort | uniq -c | sort -r

import sys, random

with open(sys.argv[1], 'r') as pos, open(sys.argv[2], 'r') as neg, open(sys.argv[3], 'w') as sent:
    sent_list = []
    for line in pos:
        sent_list.append('+1 ' + line)
    for line in neg:
        sent_list.append('-1 ' + line)
    random.shuffle(sent_list)
    for line in sent_list:
        sent.write(line)
    
