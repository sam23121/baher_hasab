from baher_hasab.lookups import DaysBookmark, EletTewsak, FastStartingDays, MonthForFasting
from typing import Tuple


class BaherHasab:
    def __init__(self, current_year: int = 2016) -> None:
        """
        Initialize the BaherHasab class with the given current year.

        Args:
            current_year (int): The current year in the Ethiopian calendar (its 7 or 8 years less than the 
                                    Geogorian calendar depending on the season of the year).
        """
        self.abiy_kemer = 532  # also known as abiy awde
        self.awde_mahtot = 76  # also known as mahkelawi awde
        self.awde_tsehay = 28  # also known as nuhase awde
        self.awde_abketa = 19
        self.old_abketa = 11
        self.amet_alem = 5500
        self.current_year = current_year

    def get_total_years(self) -> int:
        """
        Calculate the total years since the creation of the world according to the Ethiopian calendar.

        Returns:
            int: The total number of years.
        """
        return self.amet_alem + self.current_year

    def get_wember(self) -> int:
        """
        Calculate the Wember value for the current year.
        (we minus one because the year has started not finished)

        Returns:
            int: The Wember value.
        """
        total_years = self.get_total_years()
        return (total_years - 1) % self.awde_abketa

    def get_abketa(self) -> int:
        """
        Calculate the Abketa value based on the Wember value.

        Returns:
            int: The Abketa value.
        """
        wember = self.get_wember()
        abketa = ((wember * 11) % 30) if wember > 2 else wember * 11
        return abketa

    def get_metke(self) -> int:
        """
        Calculate the Metke value based on the Abketa value.

        Returns:
            int: The Metke value.
        """
        abketa = self.get_abketa()
        return 30 - abketa

    def get_first_day_of_year(self) -> str:
        """
        Calculate the first day of the year according to the Ethiopian calendar.

        Returns:
            str: The first day of the year.
        """
        total_years = self.get_total_years()
        first_day = (total_years + (total_years // 4)) % 7
        return DaysBookmark().reverse_mapping[first_day]

    def add_days(self, day: str, num_days: int) -> str:
        """
        Adds the given number of days to the specified day of the week and returns the resulting day.

        Args:
            day (str): The day of the week (e.g., 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday').
            num_days (int): The number of days to add.

        Returns:
            str: The resulting day of the week.
        """
        days_of_the_week = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        day_index = days_of_the_week.index(day)
        new_index = (day_index + num_days) % len(days_of_the_week)
        return days_of_the_week[new_index]

    def get_nenewa(self) -> Tuple[int, int]:
        """
        Calculate the Nenewa day and Metke month based on the Metke value.

        Returns:
            Tuple[int, int]: The Nenewa day and Metke month.
        """
        metke = self.get_metke()
        metke_month = 0 if metke > 15 else 30
        first_day = self.get_first_day_of_year()
        day_of_metke = self.add_days(first_day, metke_month + metke - 1)

        day_of_nenewa = getattr(EletTewsak, day_of_metke)

        nenewa_day = (metke_month + metke + day_of_nenewa) % 30

        print(f"Tir {nenewa_day}" if metke_month == 0 else f"Yekatit {nenewa_day}")

        return nenewa_day, metke_month

    def get_length_between(self, nenewa: int, fast: str) -> Tuple[int, int]:
        """
        Calculate the length between the Nenewa day and the start of a fast.

        Args:
            nenewa (int): The Nenewa day.
            fast (str): The name of the fast.

        Returns:
            Tuple[int, int]: The total length and the day of the event.
        """
        length_from_nenewa = getattr(FastStartingDays, fast) + nenewa
        day = 30 if (length_from_nenewa) % 30 == 0 else (length_from_nenewa) % 30

        return length_from_nenewa, day

    def get_event_date(self, event_name: str) -> str:
        """
        Calculate the date of an event based on the Nenewa day and the length to the event.

        Args:
            event_name (str): The name of the event.

        Returns:
            str: The date of the event.
        """
        nenewa, metke_month = self.get_nenewa()
        length_to_event, day_of_event = self.get_length_between(nenewa, event_name)

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


    def get_hudade(self) -> str:
        """
        Get the date of Hudade.

        Returns:
            str: The date of Hudade.
        """
        return self.get_event_date("hudade")

    def get_debrezeit(self) -> str:
        """
        Get the date of Debre Zeit.

        Returns:
            str: The date of Debre Zeit.
        """
        return self.get_event_date("debrezeit")

    def get_hosana(self) -> str:
        """
        Get the date of Hosana.

        Returns:
            str: The date of Hosana.
        """
        return self.get_event_date("hosana")

    def get_seklet(self) -> str:
        """
        Get the date of Seklet.

        Returns:
            str: The date of Seklet.
        """
        return self.get_event_date("seklet")

    def get_tensae(self) -> str:
        """
        Get the date of Tensae.

        Returns:
            str: The date of Tensae.
        """
        return self.get_event_date("tensae")

    def get_rekeb_kanat(self) -> str:
        """
        Get the date of Rekeb Kanat.

        Returns:
            str: The date of Rekeb Kanat.
        """
        return self.get_event_date("rekeb_kanat")

    def get_erget(self) -> str:
        """
        Get the date of Erget.

        Returns:
            str: The date of Erget holiday.
        """
        return self.get_event_date("erget")

    def get_piraklitos(self) -> str:
        """
        Get the date of Piraklitos.

        Returns:
            str: The date of Piraklitos holiday.
        """
        return self.get_event_date("piraklitos")

    def get_hawaryat(self) -> str:
        """
        Get the date of Hawaryat.

        Returns:
            str: The date of Hawaryat fast.
        """
        return self.get_event_date("hawaryat")

    def get_dehenet(self) -> str:
        """
        Get the date of Dehenet.

        Returns:
            str: The date of Dehenet fast.
        """
        return self.get_event_date("dehenet")
