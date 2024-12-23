import unittest
from search import linear_search, binary_search

class SearchTestCase(unittest.TestCase):
    def test_linear_search(self): 
        values = [4, 5, 6, 7, 3, 8, 1] 
        res = linear_search(values, 7) 
        self.assertEqual(res, 3)
        self.assertEqual(linear_search(values, 4), 0)
        

def test_binary_search(self):
    values = [4, 5, 6, 7, 3, 8, 1]
    values.sort()
    res = binary_search(values, 7) 
    self.assertEqual(res, 3)
    self.assertEqual(binary_search(values, 4), 0)
    

if __name__ == '__main__':
    unittest.main()
