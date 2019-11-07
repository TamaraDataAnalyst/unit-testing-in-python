import unittest
from crypto_data import ParseCryptoData


class testCryptoDataTest(unittest.TestCase):

    def setUp(self):
        self.data = 'crypto_data.csv' 
        self.test = ParseCryptoData(self.data)         
        self.parsed_data = self.test.read_crypto_data()

    def test_read_column_names(self):
        self.assertEqual(
            self.parsed_data[0],
            ['Date', 'Symbol','Open', 'High', 'Low', 'Close', 'Volume BTC', 'Volume USD']
            )
    
    def test_min_index_value(self):
        self.assertEqual(self.test.get_min(self.parsed_data,5),1705)

    def test_max_index_value(self):
        self.assertEqual(self.test.get_max(self.parsed_data,2), 637) 

    def test_pct_change(self):
        self.assertEqual(self.test.pct_change(self.parsed_data,2,5), 2.84)
    
    def test_read_random_values(self):
        self.assertEqual(self.parsed_data[1][0], '9/27/2019')
        self.assertEqual(self.parsed_data[51][5], '11981')
        self.assertEqual(self.parsed_data[5][7], '102332904.4')

    
if __name__ == '__main__':
    unittest.main()