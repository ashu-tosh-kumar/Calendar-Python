from exceptions import InvalidDateFormat


class Date:
    def __init__(self, date: str):
        if not self._validateDate(date):
            raise InvalidDateFormat

        self._year, self._month, self._day = map(int, date.split("-"))

    def _validateDate(self, date):
        return True

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day
