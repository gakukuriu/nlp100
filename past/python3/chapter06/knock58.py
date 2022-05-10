import sys, re
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for dependencies in root.iter('dependencies'):
    if dependencies.attrib['type'] == 'collapsed-dependencies':
        for dep in dependencies.findall('dep'):
            if dep.attrib['type'] == 'nsubj':
                verb = dep.find('governor').text
                subj = dep.find('dependent').text
                for dep2 in dependencies.findall('dep'):
                    if dep2.attrib['type'] == 'dobj' and dep2.find('governor').text == verb:
                        purp = dep2.find('dependent').text
                        print(subj + '\t' + verb + '\t' + purp)
