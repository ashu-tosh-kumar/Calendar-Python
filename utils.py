from constants import DAY, MONTH, MONTHS_WITH_31_DAYS
from exceptions import InvalidDateFormat


def isLeapYear(year: int) -> bool:
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
    def __init__(self, date: str) -> None:
        if not self._validateDate(date):
            raise InvalidDateFormat

        year, month, day = map(int, date.split("-"))
        self._year = year
        self._month = MONTH._value2member_map_[month]
        self._day = day

    def _validateDate(self, date: str) -> bool:
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
        elif MONTH._value2member_map_[month] not in MONTHS_WITH_31_DAYS:
            if day == 31:
                validFlag = False

        return validFlag

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> MONTH:
        return self._month

    @property
    def day(self) -> int:
        return self._day


def countLeapYears(date: Date) -> int:
    sol = 0
    years = date.year

    if date.month.value <= 2:
        years -= 1

    sol = years // 4
    sol -= years // 100
    sol += years // 400
    return sol


def getDaysInMonth(month: MONTH) -> int:
    # Doesn't consider leap year
    if month in MONTHS_WITH_31_DAYS:
        return 31
    elif month is MONTH.FEBRUARY:
        return 28
    else:
        return 30


def numDaysBetweenDates(baseDate: Date, actualDate: Date) -> int:
    def calculateAbsoluteDays(date: Date):
        totalDays = date.year * 365 + date.day
        for i in range(1, date.month.value):
            totalDays += getDaysInMonth(MONTH._value2member_map_[i])

        totalDays += countLeapYears(date)
        return totalDays

    totalDaysBaseDate = calculateAbsoluteDays(baseDate)
    totalDaysActualDate = calculateAbsoluteDays(actualDate)

    return totalDaysActualDate - totalDaysBaseDate
