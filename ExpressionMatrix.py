from __future__ import print_function
import sys
import glob

def createHeader(files):
    #Will need to change IDs
    header = "ID\t"
    for file in files:
        id = file.split('-')[0].split('unc.edu.')[-1]
        header = header + id + "\t"
    header = header.rstrip()
    return header

def parseGenes(files):
    geneData={}
    geneID=[]
    for file in files:
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

    return(geneData,geneID)

#search argument needs to be quoted so it isn't expanded in the command line
def main():
    search = sys.argv[1]
    files = glob.glob(search)

    output = createHeader(files)

    geneData, geneID = parseGenes(files)

    print(output)
    for gene in geneID:
        print(gene + '\t' + geneData[gene])

if __name__ == "__main__":
    main()
