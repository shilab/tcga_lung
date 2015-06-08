from __future__ import print_function
import sys
import glob

#TODO: Will have to check TCGA barcoding standard for 01A vs 01B vs 11A etc

search = sys.argv[1]
files = glob.glob(search)

output="ID\t"
miRData={}
miRID = []
for file in files:
    if file.split('-')[3]=="01A":
        id = file.split('-')[2]
    else:
        continue

    output=output+id+"\t"

    miR_file = open(file, 'r').read()
    miRs = miR_file.split('\n')
    for miR in miRs:
        if (not miR.startswith('miR')) and miR != '':
            id,_,value,_ = miR.split('\t')
            if id in miRData:
                miRData[id]=miRData[id] + "\t" + value
            else:
                miRData[id]=value
                miRID.append(id)

print(output.rstrip())
for miR in miRID:
    print(miR + '\t' + miRData[miR])
