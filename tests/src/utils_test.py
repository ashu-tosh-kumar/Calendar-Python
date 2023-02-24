import unittest

from src.constants import MONTH, PIVOT_DATE, Date
from src.exceptions import InvalidDateFormat
from src.utils import (countLeapYears, dateValidator, getActualDaysInMonth,
                   getDefaultDaysInMonth, isLeapYear, numDaysBetweenDates)


class isLeapYearTest(unittest.TestCase):
    def test_isLeapYear_should_return_true_for_2020(self):
        expectedValue = True

        actualValue = isLeapYear(2020)

        self.assertEqual(expectedValue, actualValue)

    def test_isLeapYear_should_return_true_for_2000(self):
        expectedValue = True

        actualValue = isLeapYear(2000)

        self.assertEqual(expectedValue, actualValue)

    def test_isLeapYear_should_return_false_for_3000(self):
        expectedValue = False

        actualValue = isLeapYear(3000)

        self.assertEqual(expectedValue, actualValue)

    def test_isLeapYear_should_return_false_for_2021(self):
        expectedValue = False

        actualValue = isLeapYear(2021)

        self.assertEqual(expectedValue, actualValue)


class countLeapYearsTest(unittest.TestCase):
    def test_countLeapYears_should_return_expected_value(self):
        dummyDate = Date("2022-02-28")
        expectedValue = 490

        actualValue = countLeapYears(dummyDate)

        self.assertEqual(expectedValue, actualValue)

        dummyDate = Date("2020-02-29")
        expectedValue = 489

        actualValue = countLeapYears(dummyDate)

        self.assertEqual(expectedValue, actualValue)

        dummyDate = Date("2020-03-01")
        expectedValue = 490

        actualValue = countLeapYears(dummyDate)

        self.assertEqual(expectedValue, actualValue)


class getDefaultDaysInMonthTest(unittest.TestCase):
    def test_getDefaultDaysInMonth_should_return_expected_days_for_months(self):
        self.assertEqual(getDefaultDaysInMonth(MONTH.JANUARY), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.FEBRUARY), 28)
        self.assertEqual(getDefaultDaysInMonth(MONTH.MARCH), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.APRIL), 30)
        self.assertEqual(getDefaultDaysInMonth(MONTH.MAY), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.JUNE), 30)
        self.assertEqual(getDefaultDaysInMonth(MONTH.JULY), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.AUGUST), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.SEPTEMBER), 30)
        self.assertEqual(getDefaultDaysInMonth(MONTH.OCTOBER), 31)
        self.assertEqual(getDefaultDaysInMonth(MONTH.NOVEMBER), 30)
        self.assertEqual(getDefaultDaysInMonth(MONTH.DECEMBER), 31)


class getActualDaysInMonthTest(unittest.TestCase):
    def test_getActualDaysInMonth_should_return_expected_days_for_months_for_leap_year(self):
        dummyYear = 2020
        self.assertEqual(getActualDaysInMonth(MONTH.JANUARY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.FEBRUARY, dummyYear), 29)
        self.assertEqual(getActualDaysInMonth(MONTH.MARCH, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.APRIL, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.MAY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.JUNE, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.JULY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.AUGUST, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.SEPTEMBER, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.OCTOBER, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.NOVEMBER, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.DECEMBER, dummyYear), 31)

    def test_getActualDaysInMonth_should_return_expected_days_for_months_for_non_leap_year(self):
        dummyYear = 2021
        self.assertEqual(getActualDaysInMonth(MONTH.JANUARY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.FEBRUARY, dummyYear), 28)
        self.assertEqual(getActualDaysInMonth(MONTH.MARCH, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.APRIL, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.MAY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.JUNE, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.JULY, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.AUGUST, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.SEPTEMBER, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.OCTOBER, dummyYear), 31)
        self.assertEqual(getActualDaysInMonth(MONTH.NOVEMBER, dummyYear), 30)
        self.assertEqual(getActualDaysInMonth(MONTH.DECEMBER, dummyYear), 31)


class numDaysBetweenDatesTest(unittest.TestCase):
    def test_numDaysBetweenDates_should_return_diff_of_days_between_two_dates(self):
        dummyDaseDate = Date("1752-10-01")
        dummyActualDate = Date("2385-07-01")
        expectedValue = 231106

        actualValue = numDaysBetweenDates(dummyDaseDate, dummyActualDate)

        self.assertEqual(expectedValue, actualValue)

    def test_numDaysBetweenDates_should_return_diff_of_days_between_two_dates2(self):
        dummyDaseDate = Date("2474-07-09")
        dummyActualDate = Date("2700-12-08")
        expectedValue = 82696

        actualValue = numDaysBetweenDates(dummyDaseDate, dummyActualDate)

        self.assertEqual(expectedValue, actualValue)


class dateValidatorTest(unittest.TestCase):
    def test_dateValidator_should_pass_a_valid_date(self):
        dummyDate = "2022-02-28"

        dateValidator(dummyDate, PIVOT_DATE)  # No error expected

    def test_dateValidator_should_throw_error_if_month_not_passed(self):
        dummyDate = "2022-02"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_numeric(self):
        dummyDate = "2022-ab-28"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_integer(self):
        dummyDate = "2022-2.5-28"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_month_is_not_valid(self):
        dummyDate = "2022-13-28"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid(self):
        dummyDate = "2022-12-32"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)
        
    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_leap_year(self):
        dummyDate = "2020-02-30"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_non_leap_year(self):
        dummyDate = "2021-02-29"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_day_is_not_valid_for_respective_month(self):
        dummyDate = "2021-04-31"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

    def test_dateValidator_should_throw_error_if_date_is_less_than_pivot_date(self):
        dummyDate = "1752-09-30"

        with self.assertRaises(InvalidDateFormat):
            dateValidator(dummyDate, PIVOT_DATE)

if __name__ == "__main__":
    unittest.main()
