from .lookups import FastStartingDays, MonthForFasting
from typing import Tuple


def add_days(day: str, num_days: int) -> str:
    """
    Adds the given number of days to the specified day of the week and returns the resulting day.

    Args:
        day (str): The day of the week (e.g., 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday').
        num_days (int): The number of days to add.

    Returns:
        str: The resulting day of the week.
    """
    days_of_the_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_index = days_of_the_week.index(day)
    new_index = (day_index + num_days) % len(days_of_the_week)
    return days_of_the_week[new_index]


def get_length_between(nenewe: int, fast: str) -> Tuple[int, int]:
    """
    Calculate the length between the nenewe day and the start of a fast.

    Args:
        nenewe (int): The nenewe day.
        fast (str): The name of the fast.

    Returns:
        Tuple[int, int]: The total length and the day of the event.
    """
    length_from_nenewe = getattr(FastStartingDays, fast) + nenewe
    day = 30 if (length_from_nenewe) % 30 == 0 else (length_from_nenewe) % 30

    return length_from_nenewe, day


def is_gregorian_leap_year(year: int) -> bool:
    """Check if the Gregorian year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_ethiopian_leap_year(year: int) -> bool:
    """Check if the Gregorian year is a leap year."""
    return year % 4 == 0


def calculate_gregorian_to_ethiopian(
    gregorian_year: int, gregorian_month: int, gregorian_day: int
) -> Tuple[int, int, int]:
    """Convert a Gregorian date to an Ethiopian date.

    Args:
        gregorian_year (int): The Gregorian year.
        gregorian_month (int): The Gregorian month.
        gregorian_day (int): The Gregorian day.

    Returns:
        Tuple[int, int, int]: The Ethiopian year, month, and day.
    """
    if not 1 <= gregorian_year <= 9999:
        raise ValueError("Gregorian year must be a 4-digit integer")
    if not 1 <= gregorian_month <= 12:
        raise ValueError("Gregorian month must be between 1 and 12")

    # Calculate the number of days in the Gregorian month and year
    if gregorian_month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif gregorian_month == 2:
        max_days = 28 if is_gregorian_leap_year(gregorian_year) else 29
    else:
        max_days = 30

    if not 1 <= gregorian_day <= max_days:
        raise ValueError(f"Gregorian day must be between 1 and {max_days}")

    # Difference in years between Gregorian and Ethiopian calendars
    ethio_year_diff = 7

    # New year date in Ethiopian calendar in Gregorian calendar
    if is_gregorian_leap_year(gregorian_year + 1):
        new_year_date = (9, 12)  # September 12 in a leap year
    else:
        new_year_date = (9, 11)  # September 11 in a common year

    # Calculate Ethiopian year
    diff_eight = False
    if (gregorian_month, gregorian_day) >= new_year_date:
        ethiopian_year = gregorian_year - ethio_year_diff
    else:
        ethiopian_year = gregorian_year - ethio_year_diff - 1
        diff_eight = True

    # Calculate the number of days since the last Ethiopian New Year
    gregorian_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_gregorian_leap_year(gregorian_year):
        gregorian_month_days[1] = 29

    days_in_gregorian_year = sum(gregorian_month_days)
    days_since_new_year = (
        sum(gregorian_month_days[: gregorian_month - 1]) + gregorian_day
    )
    days_since_new_year -= (
        sum(gregorian_month_days[: new_year_date[0] - 1]) + new_year_date[1]
    )

    if days_since_new_year < 0:
        days_since_new_year += days_in_gregorian_year

    # Calculate Ethiopian month and day
    ethiopian_month = days_since_new_year // 30 + 1
    # ethiopian_day = days_since_new_year % 30 + 1
    if diff_eight:
        ethiopian_day = days_since_new_year % 30
    else:
        ethiopian_day = days_since_new_year % 30 + 1
    if ethiopian_month == 13 and ethiopian_day < 5:
        ethiopian_day += 1

    if ((ethiopian_year + 1) % 4) == 0 and (gregorian_month, gregorian_day) == (
        new_year_date[0],
        new_year_date[1] - 1,
    ):
        return ethiopian_year, 13, 6

    return ethiopian_year, ethiopian_month, ethiopian_day


def calculate_ethiopian_to_gregorian(
    ethiopian_year: int, ethiopian_month: int, ethiopian_day: int
) -> Tuple[int, int, int]:
    """Convert an Ethiopian date to a Gregorian date.

    Args:
        ethiopian_year (int): The Ethiopian year.
        ethiopian_month (int): The Ethiopian month.
        ethiopian_day (int): The Ethiopian day.

    Returns:
        Tuple[int, int, int]: The Gregorian year, month, and day.
    """
    if not 1 <= ethiopian_year <= 9999:
        raise ValueError("Ethiopian year must be a 4-digit integer")
    if not 1 <= ethiopian_month <= 13:
        raise ValueError("Ethiopian month must be between 1 and 13")
    if not 1 <= ethiopian_day <= 30:
        raise ValueError("Ethiopian day must be between 1 and 30")

    # Calculate the number of days in the Ethiopian month
    max_days = 30
    if ethiopian_month == 13:
        max_days = 6 if (ethiopian_year % 4) == 3 else 5

    if not 1 <= ethiopian_day <= max_days:
        raise ValueError(f"Ethiopian day must be between 1 and {max_days}")

    # Difference in years between Gregorian and Ethiopian calendars
    ethio_year_diff = 7

    gregorian_year = ethiopian_year + ethio_year_diff

    # New year date in Ethiopian calendar in Gregorian calendar
    if is_gregorian_leap_year(gregorian_year + 1):
        new_year_date = (9, 12)  # September 12 in a leap year
    else:
        new_year_date = (9, 11)  # September 11 in a common year

    # Calculate the number of days since the Ethiopian New Year
    days_since_new_year = (ethiopian_month - 1) * 30 + (ethiopian_day - 1)

    # Calculate the Gregorian date
    gregorian_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_gregorian_leap_year(gregorian_year + 1):
        gregorian_month_days[1] = 29

    days_in_gregorian_year = sum(gregorian_month_days)
    new_year_day_of_year = (
        sum(gregorian_month_days[: new_year_date[0] - 1]) + new_year_date[1]
    )

    gregorian_day_of_year = new_year_day_of_year + days_since_new_year
    if gregorian_year - ethiopian_year == 8:
        gregorian_day_of_year -= 1

    if gregorian_day_of_year > days_in_gregorian_year:
        gregorian_day_of_year -= days_in_gregorian_year
        gregorian_year += 1

    # Calculate the month and day
    gregorian_month = 1
    while gregorian_day_of_year > gregorian_month_days[gregorian_month - 1]:
        gregorian_day_of_year -= gregorian_month_days[gregorian_month - 1]
        gregorian_month += 1

    gregorian_day = gregorian_day_of_year

    if ((ethiopian_year + 1) % 4) == 0 and (ethiopian_month, ethiopian_day) == (13, 6):
        return gregorian_year, 9, 11

    return gregorian_year, gregorian_month, gregorian_day


# @staticmethod
def get_total_days(total_years: int) -> int:
    leap_years = total_years // 4
    return (total_years - 1) * 365 + leap_years


# @staticmethod
def get_day_of_week(total_days: int) -> int:
    return (total_days % 7) + 1


# @staticmethod
def calculate_days_to_nenewe(start_day_of_week: int) -> int:
    return 128 - ((start_day_of_week + 1) % 7) + 1


# @staticmethod
def calculate_event_date(
    total_days_till_metke: int,
    days_to_event: int,
    nenewe_to_event_length: int,
    total_days: int,
) -> Tuple[int, int]:
    event_day = total_days_till_metke + days_to_event + nenewe_to_event_length
    month_of_event = ((event_day - total_days - 1) // 30) + 1
    if (event_day - total_days - 1) % 30 == 0:
        month_of_event -= 1
    day_of_event = ((event_day - total_days - 1) % 30) or 30
    return month_of_event, day_of_event


def old_get_event_date(self, event_name: str) -> str:
    """
    Calculate the date of an event based on the nenewe day and the length to the event.

    Args:
        event_name (str): The name of the event.

    Returns:
        str: The date of the event.
    """
    nenewe, metke_month = self.get_nenewe()
    length_to_event, day_of_event = self.get_length_between(nenewe, event_name)

    months = MonthForFasting()
    months = getattr(months, event_name)

    # min_value = min(months.values())

    for month, value in months.items():
        if metke_month > 0:
            if length_to_event > value:
                continue
        else:
            if length_to_event - 30 > value:
                continue
        return f"{month} {day_of_event}"
