import unittest
from pandas import DataFrame

class test_filtrados(unittest.TestCase):
    def test_segundo_filtrado(self):
        d = {"DANN_score": [0.994, 0.995, 0.998, 0.999, 1, 2], 
             "CADD_phred": [15, 17, 20, 37, 38, 17],
             "GERP++_RS": [1, 1, 2, 2, 3, 3]}
        df = DataFrame(data=d)     
        self.assertTrue(segundo_filtrado(df))

if __name__ == "__main__":
    unittest.main()