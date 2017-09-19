import unittest
import datetime
import geneticalg as genetic

class OneMaxTests(unittest.TestCase):
    def __init__(self):
        pass
    
    def test(self, length=100):
        geneset = [0, 1]
        
def get_fitness(genes):
    return genes.count(1)
    