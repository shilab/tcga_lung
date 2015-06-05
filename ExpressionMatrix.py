from __future__ import print_function
import sys
import glob

#search argument needs to be quoted so it isn't expanded in the command line
search = sys.argv[1]
files = glob.glob(search)

geneData = {}
geneID = []

output="ID\t"

for file in files:
    #Will need to change when aliquot ids are replaced by sample ids
    id = file.split('-')[0].split('unc.edu.')[-1]

    output = output+id+"\t"

    genes = open(file, 'r').read()
    genes = genes.split('\n')
    for gene in genes:
        if not (gene.startswith('gene') or gene.startswith('?')) and gene != '':
            id, value = gene.split('\t')
            id = id.split('|')[0]
            if id in geneData:
                geneData[id]=geneData[id] + "\t" + value
            else:
                geneData[id]=value
                geneID.append(id)

print(output)
for gene in geneID:
    print(gene + '\t' + geneData[gene])
