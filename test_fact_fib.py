import unittest
from fact_fib import fact, fib

class TestFactFib(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(10), 3628800)
    
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)

if __name__ == '__main__':
    unittest.main()