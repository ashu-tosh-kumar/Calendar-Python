import unittest

from src.constants import MONTH, PIVOT_DATE, Date
from src.exceptions import InvalidDateFormat
from src.utils import (
    count_leap_years,
    date_validator,
    get_actual_days_in_month,
    get_default_days_in_month,
    is_leap_year,
    num_days_between_dates,
)


class IsLeapYearTest(unittest.TestCase):
    def test_isLeapYear_should_return_true_for_2020(self):
        expected_value = True

        actual_value = is_leap_year(2020)

        self.assertEqual(expected_value, actual_value)

    def test_isLeapYear_should_return_true_for_2000(self):
        expected_value = True

        actual_value = is_leap_year(2000)

        self.assertEqual(expected_value, actual_value)

    def test_isLeapYear_should_return_false_for_3000(self):
        expected_value = False

        actual_value = is_leap_year(3000)

        self.assertEqual(expected_value, actual_value)

    def test_isLeapYear_should_return_false_for_2021(self):
        expected_value = False

        actual_value = is_leap_year(2021)

        self.assertEqual(expected_value, actual_value)


class CountLeapYearsTest(unittest.TestCase):
    def test_countLeapYears_should_return_expected_value(self):
        dummy_date = Date("2022-02-28")
        expected_value = 490

        actual_value = count_leap_years(dummy_date)

        self.assertEqual(expected_value, actual_value)

        dummy_date = Date("2020-02-29")
        expected_value = 489

        actual_value = count_leap_years(dummy_date)

        self.assertEqual(expected_value, actual_value)

        dummy_date = Date("2020-03-01")
        expected_value = 490

        actual_value = count_leap_years(dummy_date)

        self.assertEqual(expected_value, actual_value)


class GetDefaultDaysInMonthTest(unittest.TestCase):
    def test_getDefaultDaysInMonth_should_return_expected_days_for_months(self):
        self.assertEqual(get_default_days_in_month(MONTH.JANUARY), 31)
        self.assertEqual(get_default_days_in_month(MONTH.FEBRUARY), 28)
        self.assertEqual(get_default_days_in_month(MONTH.MARCH), 31)
        self.assertEqual(get_default_days_in_month(MONTH.APRIL), 30)
        self.assertEqual(get_default_days_in_month(MONTH.MAY), 31)
        self.assertEqual(get_default_days_in_month(MONTH.JUNE), 30)
        self.assertEqual(get_default_days_in_month(MONTH.JULY), 31)
        self.assertEqual(get_default_days_in_month(MONTH.AUGUST), 31)
        self.assertEqual(get_default_days_in_month(MONTH.SEPTEMBER), 30)
        self.assertEqual(get_default_days_in_month(MONTH.OCTOBER), 31)
        self.assertEqual(get_default_days_in_month(MONTH.NOVEMBER), 30)
        self.assertEqual(get_default_days_in_month(MONTH.DECEMBER), 31)


class GetActualDaysInMonthTest(unittest.TestCase):
    def test_getActualDaysInMonth_should_return_expected_days_for_months_for_leap_year(self):
        dummy_year = 2020
        self.assertEqual(get_actual_days_in_month(MONTH.JANUARY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.FEBRUARY, dummy_year), 29)
        self.assertEqual(get_actual_days_in_month(MONTH.MARCH, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.APRIL, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.MAY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.JUNE, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.JULY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.AUGUST, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.SEPTEMBER, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.OCTOBER, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.NOVEMBER, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.DECEMBER, dummy_year), 31)

    def test_getActualDaysInMonth_should_return_expected_days_for_months_for_non_leap_year(self):
        dummy_year = 2021
        self.assertEqual(get_actual_days_in_month(MONTH.JANUARY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.FEBRUARY, dummy_year), 28)
        self.assertEqual(get_actual_days_in_month(MONTH.MARCH, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.APRIL, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.MAY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.JUNE, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.JULY, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.AUGUST, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.SEPTEMBER, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.OCTOBER, dummy_year), 31)
        self.assertEqual(get_actual_days_in_month(MONTH.NOVEMBER, dummy_year), 30)
        self.assertEqual(get_actual_days_in_month(MONTH.DECEMBER, dummy_year), 31)


class NumDaysBetweenDatesTest(unittest.TestCase):
    def test_numDaysBetweenDates_should_return_diff_of_days_between_two_dates(self):
        dummy_base_date = Date("1752-10-01")
        dummy_actual_date = Date("2385-07-01")
        expected_value = 231106

        actual_value = num_days_between_dates(dummy_base_date, dummy_actual_date)

        self.assertEqual(expected_value, actual_value)

    def test_numDaysBetweenDates_should_return_diff_of_days_between_two_dates2(self):
        dummy_base_date = Date("2474-07-09")
        dummy_actual_date = Date("2700-12-08")
        expected_value = 82696

        actual_value = num_days_between_dates(dummy_base_date, dummy_actual_date)

        self.assertEqual(expected_value, actual_value)


class DateValidatorTest(unittest.TestCase):
    def test_dateValidator_should_pass_a_valid_date(self):
        dummy_date = "2022-02-28"

        date_validator(dummy_date, PIVOT_DATE)  # No error expected

    def test_dateValidator_should_throw_error_if_month_not_passed(self):
        dummy_date = "2022-02"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_numeric(self):
        dummy_date = "2022-ab-28"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_integer(self):
        dummy_date = "2022-2.5-28"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_valid(self):
        dummy_date = "2022-13-28"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid(self):
        dummy_date = "2022-12-32"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_leap_year(self):
        dummy_date = "2020-02-30"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_non_leap_year(self):
        dummy_date = "2021-02-29"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_respective_month(self):
        dummy_date = "2021-04-31"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_date_is_less_than_pivot_date(self):
        dummy_date = "1752-09-30"

        with self.assertRaises(InvalidDateFormat):
            date_validator(dummy_date, PIVOT_DATE)


if __name__ == "__main__":
    unittest.main()
