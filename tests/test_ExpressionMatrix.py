from ExpressionMatrix import *
from nose.tools import raises
import unittest

def test_header():
    assert create_header(['TCGA-97-8552-01A-11R-2403-07.1899074.rsem.genes.normalized_results', 'TCGA-78-7156-01A-11R-2039-07.1092613.rsem.genes.normalized_results']) == 'ID\t8552\t7156'

@raises(SystemExit)
def test_empty():
    create_header([])

def test_gene_id():
    _, gene_ids = parse_genes(['tests/genes1', 'tests/genes2'])
    assert gene_ids == ['A1BG', 'A1CF', 'A2BP1']

def test_gene_ata():
    gene_data, _ = parse_genes(['tests/genes1', 'tests/genes2'])
    assert gene_data['A1BG'] == '39.7563\t39.7563'
    assert gene_data['A1CF'] == '0.2593\t0.2593'
    assert gene_data['A2BP1'] == '0.0000\t0.0000'
