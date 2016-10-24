import unittest
from pandas import DataFrame
from numpy import array

class test_filtrados(unittest.TestCase):
    def test_segundo_filtrado(self):
        d = {"DANN_score": [0.994, 0.995, 0.998, 0.999, 1, 2], 
             "CADD_phred": [15, 17, 20, 37, 38, 17],
             "GERP++_RS": [1, 1, 2, 2, 3, 3]}
        df = DataFrame(data=d)     
        self.assertTrue(segundo_filtrado(df))
    def test_segundo_filtrado_correcto(self):
        d = {"DANN_score": [0.994, 0.995, 0.998, 0.999, 1, 2], 
             "CADD_phred": [15, 17, 20, 37, 38, 17],
             "GERP++_RS": [1, 1, 2, 2, 3, 3]}
        df = DataFrame(data=d) 
        sg = array([37.0, 0.999, 2.0])
        self.assertEqual(3, len(segundo_filtrado(df)))
        self.assertEqual(sg.all(), segundo_filtrado(df)[0].values.all())

if __name__ == "__main__":
    unittest.main()