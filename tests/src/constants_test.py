import unittest

from src.constants import DAY, MONTH, MONTHS_WITH_31_DAYS, PIVOT_DATE, PIVOT_DAY, Date


class ConstantsTest(unittest.TestCase):
    def test_DAY_should_contain_7_days(self):
        self.assertEqual(7, len(DAY))

    def test_MONTH_should_contain_12_months(self):
        self.assertEqual(12, len(MONTH))

    def test_Date_should_parse_valid_date(self):
        dummyDate = "2022-02-28"
        Date(dummyDate)  # No error expected

    def test_Date_should_have_year_month_day_properties(self):
        dummyDate = "2022-02-28"
        dateObject = Date(dummyDate)

        self.assertEqual(2022, dateObject.year)
        self.assertEqual(MONTH.FEBRUARY, dateObject.month)
        self.assertEqual(28, dateObject.day)

    def test_Date_should_allow_setting_of_day(self):
        dummyDate = "2022-02-28"
        dateObject = Date(dummyDate)

        dateObject.day = 15

        self.assertEqual(15, dateObject.day)

    def test_Date_should_provide_original_date_when_printed(self):
        dummyDate = "2022-02-28"
        dateObject = Date(dummyDate)

        self.assertEqual(str(dateObject), "2022-2-28")

    def test_PIVOT_DATE(self):
        ExpectedDate = Date("1752-10-01")

        self.assertEqual(ExpectedDate.year, PIVOT_DATE.year)
        self.assertEqual(ExpectedDate.month, PIVOT_DATE.month)
        self.assertEqual(ExpectedDate.day, PIVOT_DATE.day)

    def test_PIVOT_DAY(self):
        self.assertEqual(DAY.SUNDAY, PIVOT_DAY)

    def test_MONTHS_WITH_31_DAYS_should_contain_7_months(self):
        self.assertEqual(7, len(MONTHS_WITH_31_DAYS))


if __name__ == "__main__":
    unittest.main()
