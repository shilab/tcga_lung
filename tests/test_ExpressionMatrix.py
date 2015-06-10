from ExpressionMatrix import *
import unittest

def test_header():
    assert create_header(['unc.edu.ff74b4c6-e938-4a40-ab1a-84525349a62e.1229487.rsem.genes.normalized_results', 'unc.edu.8719f9af-0876-4ec6-a4dc-4178ad964349.1643074.rsem.genes.normalized_results']) == "ID\tff74b4c6\t8719f9af"

def test_gene_id():
    _, gene_ids = parse_genes(['tests/genes1', 'tests/genes2'])
    assert gene_ids == ['A1BG', 'A1CF', 'A2BP1']

def test_gene_ata():
    gene_data, _ = parse_genes(['tests/genes1', 'tests/genes2'])
    assert gene_data['A1BG'] == "39.7563\t39.7563"
    assert gene_data['A1CF'] == "0.2593\t0.2593"
    assert gene_data['A2BP1'] == "0.0000\t0.0000"
