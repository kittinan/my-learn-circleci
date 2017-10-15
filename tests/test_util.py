import unittest
from kittinan import util

class TestUtil(unittest.TestCase):

    def test_add(self):
        x = 1337
        y = 1337
        result = util.add_number(x, y)
        expected = x + y
        self.assertEqual(result, expected)

    def test_minus(self):
        x = 1337
        y = 124
        result = util.minus_number(x, y)
        expected = x - y
        self.assertEqual(result, expected)

    def test_hahaha(self):
        result = util.hahaha_number()
        expected = 555
        self.assertEqual(result, expected)

    def test_kittinan(self):
        result = util.kittinan_number()
        expected = 124
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
