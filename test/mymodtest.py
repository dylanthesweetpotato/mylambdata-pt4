import unittest

from my_lambdata.my_mod import enlarge


x = 5
print(x, "Enlarge", enlarge(x))

class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)

if __name__ == '__main__':
    unittest.main()