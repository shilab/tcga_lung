from miRMatrix import *
from nose.tools import raises
import unittest

def test_header():
    assert create_header(['TCGA-55-6985-01A-11H-1948-13.mirna.quantification.txt','TCGA-S2-AA1A-01A-12H-A39B-13.mirna.quantification.txt']) == 'ID\t6985\tAA1A'
    assert create_header(['TCGA-55-6985-01A-11H-1948-13.mirna.quantification.txt','TCGA-S2-AA1A-11A-12H-A39B-13.mirna.quantification.txt']) == 'ID\t6985'

@raises(SystemExit)
def test_empty():
    create_header([])

def test_mirna_ids():
    _, mirna_ids = parse_mirna(['tests/miRNA1','tests/miRNA2'])
    assert mirna_ids == ['hsa-let-7a-1','hsa-let-7a-2','hsa-let-7a-3']

def test_mirna_data():
    mirna_data, _ = parse_mirna(['tests/miRNA1','tests/miRNA2'])
    assert mirna_data['hsa-let-7a-1'] == '9870.569273\t3977.302846'
    assert mirna_data['hsa-let-7a-2'] == '19756.504636\t7969.303424'
    assert mirna_data['hsa-let-7a-3'] == '9926.316021\t4004.529793'
