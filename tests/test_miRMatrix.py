from miRMatrix import *
import unittest

def test_header():
    assert createHeader(['TCGA-55-6985-01A-11H-1948-13.mirna.quantification.txt','TCGA-S2-AA1A-01A-12H-A39B-13.mirna.quantification.txt']) == "ID\t6985\tAA1A"
    assert createHeader(['TCGA-55-6985-01A-11H-1948-13.mirna.quantification.txt','TCGA-S2-AA1A-11A-12H-A39B-13.mirna.quantification.txt']) == "ID\t6985"

def test_mirID():
    _, mirID = parsemiR(['tests/miRNA1','tests/miRNA2'])
    assert mirID == ['hsa-let-7a-1','hsa-let-7a-2','hsa-let-7a-3']

def test_miRData():
    miRData, _ = parsemiR(['tests/miRNA1','tests/miRNA2'])
    assert miRData['hsa-let-7a-1']=="9870.569273\t3977.302846"
    assert miRData['hsa-let-7a-2']=="19756.504636\t7969.303424"
    assert miRData['hsa-let-7a-3']=="9926.316021\t4004.529793"
