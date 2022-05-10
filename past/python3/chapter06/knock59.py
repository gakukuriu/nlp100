import sys, re
import xml.etree.ElementTree as ET
from sexpdata import loads, dumps

tree = ET.parse(sys.argv[1])
root = tree.getroot()

def slistPrint(slist):
    if isinstance(slist[1], list):
        for el in slist[1:]:
            slistPrint(el)
    else:
        print(dumps(slist[1]).replace('\\', ''), end=' ')        
        
def slistRecursiveSearch(slist, query):
    if dumps(slist[0]) == query:
        slistPrint(slist)
        print()
    if isinstance(slist[1], list):
        for el in slist[1:]:
            slistRecursiveSearch(el, query)
            
        
for parse in root.iter('parse'):
    try:
        slist = loads(parse.text)
        slistRecursiveSearch(slist, 'NP')
    except IndexError:
        print('--------- Error Occured!!! ---------')
