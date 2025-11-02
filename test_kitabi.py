import unittest
from kitabi import reverse_string

class TestKitabi(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

if __name__ == "__main__":
    unittest.main()
