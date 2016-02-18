from xml.dom import minidom
import os
import csv
from os import getcwd
from os import listdir
import sys

import operator

files = os.listdir('hmdb_metabolites')
#remove .DS_Store
if (files[0]=='.DS_Store'):
    files.pop(0)

if 'hmdb_metabolites.xml' in files:
    print "please"
    sys.exit()

f = open('HMDBMappingFile.tsv', 'w')
mapping = dict()
mapping2 = dict()
for x in range(0,len(files)):
#for x in range(0,100):
   xmldoc = minidom.parse('hmdb_metabolites/'+ files[x])
   try:
      chemical_formula = xmldoc.getElementsByTagName('chemical_formula')[0].childNodes[0].nodeValue
   except:
      chemical_formula = "no_entry"
   try:
      monisotopic_moleculate_weight = xmldoc.getElementsByTagName('monisotopic_moleculate_weight')[0].childNodes[0].nodeValue
   except:
      monisotopic_moleculate_weight = 0
   accession = xmldoc.getElementsByTagName('accession')[0].childNodes[0].nodeValue
   #chemical_formula = chemical_formula.encode('ascii')
   #accession = accession.encode('ascii')
   mapping2[chemical_formula] = float(monisotopic_moleculate_weight)
   if not chemical_formula in mapping:
      #print(chemical_formula)
      mapping[chemical_formula] = ["HMDB:" + accession]
   else:
      #print(type(chemical_formula))
      mapping[chemical_formula].append('HMDB:'+accession)
   #(chemical_formula)
   #print(monisotopic_moleculate_weight)

mapping['C10(2)H3(1)H16NO4'] = ["EXTRA:EXTRA001"]
mapping['C16H18N4O2'] = ["EXTRA:EXTRA002"]
mapping['C12(2)H6(1)H8N4O4S'] = ["EXTRA:EXTRA003"]
mapping['C23(2)H3(1)H42NO4'] = ["EXTRA:EXTRA006"]
mapping['C25(2)H3(1)H46NO4'] = ["EXTRA:EXTRA007"]
mapping2['C10(2)H3(1)H16NO4'] = 220.1502383412
mapping2['C16H18N4O2'] = 298.1429758428
mapping2['C12(2)H6(1)H8N4O4S'] = 316.111236124
mapping2['C23(2)H3(1)H42NO4'] = 402.3536891758
mapping2['C25(2)H3(1)H46NO4'] = 430.3849893042
mapping['C32H41NO2'].append("EXTRA:EXTRA005")
mapping['C33H40N2O9'].append("EXTRA:EXTRA004")
sorted_x = sorted(mapping2.items(), key=operator.itemgetter(1))

f.write('database_name')
f.write('\t')
f.write('HMDB')
f.write('\n')
f.write('database_version')
f.write('\t')
f.write('3.6')
f.write('\n')

for (key,weight) in sorted_x:
   if key=="no_entry":
      continue
   f.write(str(weight))
   f.write('\t')
   f.write(key)
   for x in mapping[key]:
      f.write('\t')
      f.write(x)
   f.write('\n')
