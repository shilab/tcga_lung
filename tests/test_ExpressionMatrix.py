from ExpressionMatrix import *
import unittest

def test_header():
    assert createHeader(['unc.edu.ff74b4c6-e938-4a40-ab1a-84525349a62e.1229487.rsem.genes.normalized_results','unc.edu.8719f9af-0876-4ec6-a4dc-4178ad964349.1643074.rsem.genes.normalized_results']) == "ID\tff74b4c6\t8719f9af"

def test_geneID():
    _, geneID = parseGenes(['tests/genes1','tests/genes2'])
    assert geneID == ['A1BG','A1CF','A2BP1']

def test_geneData():
    geneData, _ = parseGenes(['tests/genes1','tests/genes2'])
    assert geneData['A1BG']=="39.7563\t39.7563"
    assert geneData['A1CF']=="0.2593\t0.2593"
    assert geneData['A2BP1']=="0.0000\t0.0000"
