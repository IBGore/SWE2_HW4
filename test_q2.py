import unittest
import q2


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q2.listAve([2,4,6]), 4)

    def test2(self):
        self.assertAlmostEqual(q2.listAve([1.1, 2.2, 3.3]), 2.2) #almost equal deals with float rounding inconsistency

    def test3(self):
        with self.assertRaises(AssertionError):
            q2.listAve([])

    def test4(self):
        with self.assertRaises(AssertionError):
            q2.listAve(["str", 3])

if __name__ == '__main__':
    unittest.main(verbosity=2)