import unittest
from unittest.mock import patch

from api.src.exceptions import InvalidDateFormat
from api.src.get_date_matrix import get_date_matrix


class GetDateMatrixTest(unittest.TestCase):
    @patch("api.src.get_date_matrix.utils")
    def test_getDateMatrix_should_raise_exception_for_invalid_date(self, stub_utils):
        dummy_date = "2022-13-15"  # Invalid month 13
        stub_utils.date_validator.side_effect = InvalidDateFormat("unittest-date-validation-exception")

        with self.assertRaises(InvalidDateFormat):
            get_date_matrix(dummy_date)

    @patch("api.src.get_date_matrix.utils")
    def test_getDateMatrix_should_return_expected_date_matrix(self, stub_utils):
        dummy_date = "2022-02-28"
        # The code in get_date_matrix.py makes date as 1, so this value wouldn't be the actual different between dummy_date and PIVOT_DATE
        stub_utils.num_days_between_dates.return_value = 98373
        stub_utils.get_actual_days_in_month.side_effect = [31, 28]
        expected_value = [
            [30, 31, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26],
            [27, 28, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12],
        ]

        actual_value = get_date_matrix(dummy_date)

        self.assertEqual(expected_value, actual_value)

    @patch("api.src.get_date_matrix.utils")
    def test_getDateMatrix_should_return_expected_date_matrix_for_leap_month(self, stub_utils):
        dummy_date = "2020-02-28"
        # The code in get_date_matrix.py makes date as 1, so this value wouldn't be the actual different between dummy_date and PIVOT_DATE
        stub_utils.num_days_between_dates.return_value = 97642
        stub_utils.get_actual_days_in_month.side_effect = [31, 29]
        expected_value = [
            [26, 27, 28, 29, 30, 31, 1],
            [2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22],
            [23, 24, 25, 26, 27, 28, 29],
            [1, 2, 3, 4, 5, 6, 7],
        ]

        actual_value = get_date_matrix(dummy_date)

        self.assertEqual(expected_value, actual_value)

    @patch("api.src.get_date_matrix.utils")
    def test_getDateMatrix_should_return_expected_date_matrix_for_non_leap_month(
        self,
        stub_utils,
    ):
        dummy_date = "2020-03-28"
        # The code in get_date_matrix.py makes date as 1, so this value wouldn't be the actual different between dummy_date and PIVOT_DATE
        stub_utils.num_days_between_dates.return_value = 97671
        stub_utils.get_actual_days_in_month.side_effect = [29, 31]
        expected_value = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 1, 2, 3, 4],
            [5, 6, 7, 8, 9, 10, 11],
        ]

        actual_value = get_date_matrix(dummy_date)

        self.assertEqual(expected_value, actual_value)

    @patch("api.src.get_date_matrix.utils")
    def test_getDateMatrix_should_return_expected_date_matrix_for_a_random_date(self, stub_utils):
        dummy_date = "2385-07-07"
        # The code in get_date_matrix.py makes date as 1, so this value wouldn't be the actual different between dummy_date and PIVOT_DATE
        stub_utils.num_days_between_dates.return_value = 231106
        stub_utils.get_actual_days_in_month.side_effect = [30, 31]
        expected_value = [
            [30, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
            [14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27],
            [28, 29, 30, 31, 1, 2, 3],
            [4, 5, 6, 7, 8, 9, 10],
        ]

        actual_value = get_date_matrix(dummy_date)

        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()
