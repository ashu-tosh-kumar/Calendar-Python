import unittest
from unittest.mock import patch

from src.exceptions import InvalidDateFormat
from src.model import getDateMatrix


class getDateMatrixTest(unittest.TestCase):
    @patch("model.dateValidator")
    def test_getDateMatrix_should_raise_exception_for_invalid_date(self, stubDateValidator):
        dummyDate = "2022-13-15"  # Invalid month 13
        stubDateValidator.side_effect = InvalidDateFormat(
            "unittest-date-validation-exception")

        with self.assertRaises(InvalidDateFormat):
            getDateMatrix(dummyDate)

    @patch("model.getActualDaysInMonth")
    @patch("model.numDaysBetweenDates")
    @patch("model.dateValidator")
    def test_getDateMatrix_should_return_expected_date_matrix(self, stubDateValidator, stubNumDaysBetweenDates, stubGetActualDaysInMonth):
        dummyDate = "2022-02-28"
        # The code in model.py makes date as 1, so this value wouldn't be the actual different between dummyDate and PIVOT_DATE
        stubNumDaysBetweenDates.return_value = 98373
        stubGetActualDaysInMonth.side_effect = [31, 28]
        expectedValue = [
            [30, 31, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26],
            [27, 28, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12]
        ]

        actualValue = getDateMatrix(dummyDate)

        self.assertEqual(expectedValue, actualValue)

    @patch("model.getActualDaysInMonth")
    @patch("model.numDaysBetweenDates")
    @patch("model.dateValidator")
    def test_getDateMatrix_should_return_expected_date_matrix_for_leap_month(self, stubDateValidator, stubNumDaysBetweenDates, stubGetActualDaysInMonth):
        dummyDate = "2020-02-28"
        # The code in model.py makes date as 1, so this value wouldn't be the actual different between dummyDate and PIVOT_DATE
        stubNumDaysBetweenDates.return_value = 97642
        stubGetActualDaysInMonth.side_effect = [31, 29]
        expectedValue = [
            [26, 27, 28, 29, 30, 31, 1],
            [2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22],
            [23, 24, 25, 26, 27, 28, 29],
            [1, 2, 3, 4, 5, 6, 7]
        ]

        actualValue = getDateMatrix(dummyDate)

        self.assertEqual(expectedValue, actualValue)

    @patch("model.getActualDaysInMonth")
    @patch("model.numDaysBetweenDates")
    @patch("model.dateValidator")
    def test_getDateMatrix_should_return_expected_date_matrix_for_non_leap_month(self, stubDateValidator, stubNumDaysBetweenDates, stubGetActualDaysInMonth):
        dummyDate = "2020-03-28"
        # The code in model.py makes date as 1, so this value wouldn't be the actual different between dummyDate and PIVOT_DATE
        stubNumDaysBetweenDates.return_value = 97671
        stubGetActualDaysInMonth.side_effect = [29, 31]
        expectedValue = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 1, 2, 3, 4],
            [5, 6, 7, 8, 9, 10, 11]
        ]

        actualValue = getDateMatrix(dummyDate)

        self.assertEqual(expectedValue, actualValue)

    @patch("model.getActualDaysInMonth")
    @patch("model.numDaysBetweenDates")
    @patch("model.dateValidator")
    def test_getDateMatrix_should_return_expected_date_matrix_for_a_random_date(self, stubDateValidator, stubNumDaysBetweenDates, stubGetActualDaysInMonth):
        dummyDate = "2385-07-07"
        # The code in model.py makes date as 1, so this value wouldn't be the actual different between dummyDate and PIVOT_DATE
        stubNumDaysBetweenDates.return_value = 231106
        stubGetActualDaysInMonth.side_effect = [30, 31]
        expectedValue = [
            [30, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
            [14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27],
            [28, 29, 30, 31, 1, 2, 3],
            [4, 5, 6, 7, 8, 9, 10]
        ]

        actualValue = getDateMatrix(dummyDate)

        self.assertEqual(expectedValue, actualValue)


if __name__ == "__main__":
    unittest.main()
