# TCGA LUAD

[![Build Status](https://travis-ci.org/shilab/tcga_tools.svg)](https://travis-ci.org/shilab/tcga_tools)

Scripts to preprocess TCGA data

ExpressionMatrix.py combines individual expression files into one gene expression matrix.
Usage:
```
python ExpressionMatrix.py 'path/to/data/*rsem.genes.normalized_results'
```
miRMatrix.py combines individual miRNA expression files into one miRNA expression matrix. 
```
python miRMatrix.py 'path/to/data/*mirna.quantification.txt'
```

Notes: The file globs need to be quoted so they aren't automatically expanded by the shell. 
