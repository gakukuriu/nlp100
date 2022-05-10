import sys, re
import xml.etree.ElementTree as ET
from graphviz import Digraph

tree = ET.parse(sys.argv[1])
root = tree.getroot()
filenumber = 0

for dependencies in root.iter('dependencies'):
    if dependencies.attrib['type'] == 'collapsed-dependencies':
        g = Digraph('G', filename='gvs/knock57.gv_' + str(filenumber))
        filenumber += 1
        for dep in dependencies.findall('dep'):
            if not (dep.find('governor').text in ',.' or dep.find('dependent').text in ',.'):
                g.edge(dep.find('governor').text, dep.find('dependent').text)
        g.view()
