from xml.dom import minidom
import os
import csv
from os import getcwd
from os import listdir
import sys
import re

files = os.listdir('hmdb_metabolites')
#remove .DS_Store
if (files[0]=='.DS_Store'):
    files.pop(0)

if 'hmdb_metabolites.xml' in files:
    print "please"
    sys.exit()

f = open('HMDB2StructMapping.tsv', 'w')
for x in range(0,len(files)):
#for x in range(0,10):
   xmldoc = minidom.parse('hmdb_metabolites/'+ files[x])
   accession = xmldoc.getElementsByTagName('accession')[0].childNodes[0].nodeValue
   name = xmldoc.getElementsByTagName('name')[0].childNodes[0].nodeValue
   try:
      smiles = xmldoc.getElementsByTagName('smiles')[0].childNodes[0].nodeValue
   except:
      smiles = ""
   try:
      inchi = xmldoc.getElementsByTagName('inchi')[0].childNodes[0].nodeValue
   except:
      inchi = ""
   if( not inchi and not smiles):
      continue
   f.write("HMDB:"+accession + "\t")
   f.write(name.encode('utf-8') + "\t")
   f.write(smiles + "\t")
   f.write(inchi + "\t")
   f.write("\n")

f2 = open('extras.tsv', 'r')
extras = f2.readlines()
for line in extras:
	elements = re.split(r'\t+', line)
	for element in elements[:-1]:
		f.write(element)
		f.write('\t')
	f.write(elements[-1])

f.close()
