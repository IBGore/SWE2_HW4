import unittest
import q1


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q1.vol(3, 2, 5), 30)

    def test2(self):
        self.assertAlmostEqual(q1.vol(1.1, 2.2, 3.3), 7.986) #almost equal deals with float rounding inconsistency

    def test3(self):
        with self.assertRaises(AssertionError):
            q1.vol(-1, 2, 3)

    def test4(self):
        with self.assertRaises(AssertionError):
            q1.vol("str", 2, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)