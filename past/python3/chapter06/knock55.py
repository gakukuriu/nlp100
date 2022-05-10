import sys, re
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
for tokens in root.iter('tokens'):
    for token in tokens.findall('token'):
        if 'PERSON' == token.find('NER').text:
            print(token.find('word').text)
