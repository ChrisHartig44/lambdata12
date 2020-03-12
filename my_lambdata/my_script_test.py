# test/my_mod_test.py
import unittest
from my_lambdata.my_script.py import shrink
class TestMyMod(unittest.TestCase):
    def test_enlarge(self):
        self.assertEqual(shrink(80), 60)
if __name__ == '__main__':
    unittest.main()