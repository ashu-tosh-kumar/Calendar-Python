import unittest

from exceptions import InvalidDateFormat


class InvalidDateFormatTest(unittest.TestCase):
    def test_InvalidDateFormat_should_exist(self):
        with self.assertRaises(InvalidDateFormat):
            raise InvalidDateFormat


if __name__ == "__main__":
    unittest.main()
