from exceptions import InvalidDateFormat


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


class Date:
    def __init__(self, date: str):
        if not self._validateDate(date):
            raise InvalidDateFormat

        self._year, self._month, self._day = map(int, date.split("-"))

    def _validateDate(self, date):
        monthsWith31Days = {1, 3, 5, 7, 8, 10, 12}

        validFlag = True
        if len(date) > 10:
            validFlag = False

        if date[4] != "-" or date[7] != "-":
            validFlag = False

        try:
            year, month, day = map(int, date.split("-"))
        except:
            validFlag = False

        if int(year) != year or int(month) != month or int(day) != day:
            validFlag = False

        if month < 0 or month > 12:
            validFlag = False

        if day < 0 or day > 31:
            validFlag = False

        if month == 2:
            if isLeapYear(year):
                if day > 29:
                    validFlag = False
            else:
                if day > 28:
                    validFlag = False
        elif month not in monthsWith31Days:
            if day == 31:
                validFlag = False

        return validFlag

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day
