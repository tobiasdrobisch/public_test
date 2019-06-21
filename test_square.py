#Testfile um CircleCI auszuprobieren

import unittest
import square

class KnownValues(unittest.TestCase):
    def test_square_for_10(self):
        result = square.square(10)
        expected = 100
        self.assertEqual(expected, result)

#Run the Test
if __name__ == '__main__':
        unittest.main()
