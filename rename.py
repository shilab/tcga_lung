import os
import sys
import re
import shutil

aliquot_file = sys.argv[1]
path = sys.argv[2]
newpath = sys.argv[3]

new_dict = {}

with open(aliquot_file, 'r') as af:
    for line in af:
        temp = line.split('\t')
        new_name = temp[2]
        old = temp[3]
        new_dict[old] = new_name

for filename in os.listdir(path):
    if 'rsem' not in filename:
        continue
    temp = filename.split('unc.edu.')[1].split('.')
    filename = temp[0]
    extension = ('.').join(temp[1:])
    if filename in new_dict:
         old = path + 'unc.edu.' + filename +'.' + extension
         new = newpath + new_dict[filename] + '.' + extension
         shutil.copyfile(old, new)
