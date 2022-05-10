import sys, re
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
for word in root.iter('word'):
    print(word.text)
