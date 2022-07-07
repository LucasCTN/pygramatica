import unittest, csv
import flexão

class TestNumero(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_flexao_numero_automatico(self):
        with open("testes.csv") as file:
            tsv_file = csv.reader(file)
            for line in tsv_file:
                singular = line[0]
                plural = line[1]
                self.assertEqual(flexão.plural(singular), plural)
                self.assertEqual(flexão.singular(plural), singular)

if __name__ == '__main__':
    unittest.main()