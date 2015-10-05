from __future__ import print_function
import sys
import glob

#TODO: Will have to check TCGA barcoding standard for 01A vs 01B vs 11A etc

def create_header(files):
    header = 'ID\t'

    if len(files) == 0:
        print('No files found in the glob')
        sys.exit()

    for filename in files:
        if filename.split('-')[3] == '01A':
            sample_id = filename.split('-')[2]
        else:
            continue
        header = header + sample_id + '\t'
    header = header.rstrip()
    return header

def parse_mirna(files):
    mirna_data = {}
    mirna_ids = []

    for filename in files:
        mirna_file = open(filename, 'r').read()
        mirnas = mirna_file.split('\n')
        for mirna in mirnas:
            if (not mirna.startswith('miR')) and mirna != '':
                mirna_id, _, value, _ = mirna.split('\t')
                if mirna_id in mirna_data:
                    mirna_data[mirna_id] = mirna_data[mirna_id] + '\t' + value
                else:
                    mirna_data[mirna_id] = value
                    mirna_ids.append(mirna_id)

    return(mirna_data, mirna_ids)

def main():
    search = sys.argv[1]
    files = glob.glob(search)

    output = create_header(files)

    mirna_data, mirna_ids = parse_mirna(files)

    print(output)
    for mirna in mirna_ids:
        print(mirna + '\t' + mirna_data[mirna])

if __name__ == '__main__':
    main()
