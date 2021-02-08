import unittest
import q3


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(q3.fullName("Bradley", "Gore"), "Bradley Gore")

    def test2(self):
        with self.assertRaises(AssertionError):
            q3.fullName(1, "Name")

    def test3(self):
        with self.assertRaises(AssertionError):
            q3.fullName("", "Name")


if __name__ == '__main__':
    unittest.main(verbosity=2)