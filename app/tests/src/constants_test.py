import unittest

from app.src.constants import (
    DAY,
    MONTH,
    MONTHS_WITH_31_DAYS,
    PIVOT_DATE,
    PIVOT_DAY,
    Date,
)


class ConstantsTest(unittest.TestCase):
    def test_DAY_should_contain_7_days(self):
        self.assertEqual(7, len(DAY))

    def test_MONTH_should_contain_12_months(self):
        self.assertEqual(12, len(MONTH))

    def test_Date_should_parse_valid_date(self):
        dummy_date = "2022-02-28"
        Date(dummy_date)  # No error expected

    def test_Date_should_have_year_month_day_properties(self):
        dummy_date = "2022-02-28"
        date_object = Date(dummy_date)

        self.assertEqual(2022, date_object.year)
        self.assertEqual(MONTH.FEBRUARY, date_object.month)
        self.assertEqual(28, date_object.day)

    def test_Date_should_allow_setting_of_day(self):
        dummy_date = "2022-02-28"
        date_object = Date(dummy_date)

        date_object.day = 15

        self.assertEqual(15, date_object.day)

    def test_Date_should_provide_original_date_when_printed(self):
        dummy_date = "2022-02-28"
        date_object = Date(dummy_date)

        self.assertEqual(str(date_object), "2022-2-28")

    def test_PIVOT_DATE(self):
        expected_date = Date("1752-10-01")

        self.assertEqual(expected_date.year, PIVOT_DATE.year)
        self.assertEqual(expected_date.month, PIVOT_DATE.month)
        self.assertEqual(expected_date.day, PIVOT_DATE.day)

    def test_PIVOT_DAY(self):
        self.assertEqual(DAY.SUNDAY, PIVOT_DAY)

    def test_MONTHS_WITH_31_DAYS_should_contain_7_months(self):
        self.assertEqual(7, len(MONTHS_WITH_31_DAYS))


if __name__ == "__main__":
    unittest.main()
