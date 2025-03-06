from .lookups import (
    DaysBookmark,
    EletTewsak,
    FastStartingDays,
    Wengelawyan,
    EthiopianCalendarMonths,
)
from .helper import (
    add_days,
    get_total_days,
    get_day_of_week,
    calculate_days_to_nenewe,
    calculate_event_date,
    calculate_ethiopian_to_gregorian,
    calculate_gregorian_to_ethiopian,
)
from typing import Tuple


class BaherHasab:
    def __init__(self, given_year: int = 2016) -> None:
        """
        Initialize the BaherHasab class with the given current year.

        Args:
            given_year (int): The current year in the Ethiopian calendar (its 7 or 8 years less than the
                                    Geogorian calendar depending on the season of the year).
        """
        self._abiy_kemer = 532  # also known as abiy awde
        self._awde_mahtot = 76  # also known as mahkelawi awde
        self._awde_tsehay = 28  # also known as nuhase awde
        self._awde_abketa = 19
        self._old_abketa = 11
        self._amet_alem = 5500
        self._given_year = given_year

    def __str__(self) -> str:
        total_years = self.get_total_years()
        abiy_kemer, abiy_kemer_passed_years, abiy_kemer_remaining_years = self.get_awde_kemer()
        awde_mahtot, awde_mahtot_passed_years, awde_mahtot_remaining_years = self.get_awde_mahtot()
        awde_tsehay, awde_tsehay_passed_years, awde_tsehay_remaining_years = self.get_awde_tsehay()
        wember = self.get_wember()
        abketa = self.get_abketa()
        metke = self.get_metke()
        nenewe = self.get_nenewe()
        hudade = self.get_hudade()
        debrezeit = self.get_debrezeit()
        hosana = self.get_hosana()
        seklet = self.get_seklet()
        tensae = self.get_tensae()
        rekeb_kanat = self.get_rekeb_kanat()
        erget = self.get_erget()
        piraklitos = self.get_piraklitos()
        hawaryat = self.get_hawaryat()
        

        return (
            f"BaherHasab Summary:\n"
            f"Total Years: {total_years}\n"
            f"Wember: {wember}\n"
            f"Abketa: {abketa}\n"
            f"Metke: {metke}\n"
            f"Nenewe: {nenewe}\n"
            f"Hudade: {hudade}\n"
            f"Debrezeit: {debrezeit}\n"
            f"Hosana: {hosana}\n"
            f"Seklet: {seklet}\n"
            f"Tensae: {tensae}\n"
            f"Rekeb Kanat: {rekeb_kanat}\n"
            f"Erget: {erget}\n"
            f"Piraklitos: {piraklitos}\n"
            f"Hawaryat: {hawaryat}\n"
            f"Abiy Kemer: {abiy_kemer} (Passed: {abiy_kemer_passed_years}, Remaining: {abiy_kemer_remaining_years})\n"
            f"Awde Mahtot: {awde_mahtot} (Passed: {awde_mahtot_passed_years}, Remaining: {awde_mahtot_remaining_years})\n"
            f"Awde Tsehay: {awde_tsehay} (Passed: {awde_tsehay_passed_years}, Remaining: {awde_tsehay_remaining_years})"
        )
    

    def get_total_years(self) -> int:
        """
        Calculate the total years since the creation of the world according to the Ethiopian calendar.

        Returns:
            int: The total number of years.
        """
        return self._amet_alem + self._given_year

    def get_wember(self) -> int:
        """
        Calculate the Wember value for the current year.
        (we minus one because the year has started not finished)

        Returns:
            int: The Wember value.
        """
        total_years = self.get_total_years()
        return (total_years - 1) % self._awde_abketa

    def get_abketa(self) -> int:
        """
        Calculate the Abketa value based on the Wember value.

        Returns:
            int: The Abketa value.
        """
        wember = self.get_wember()
        abketa = (wember * 11) % 30
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

    def get_nenewe_date(self) -> Tuple[int, int]:
        """
        Calculate the nenewe day and Metke month based on the Metke value.

        Returns:
            Tuple[int, int]: The nenewe day and Metke month.
        """
        metke = self.get_metke()
        metke_month = 0 if metke > 13 else 30
        first_day = self.get_first_day_of_year()
        day_of_metke = add_days(first_day, metke_month + metke - 1)
        day_of_nenewe = getattr(EletTewsak, day_of_metke)

        nenewe_day = (metke_month + metke + day_of_nenewe) % 30

        return nenewe_day, metke_month
    

    def get_nenewe(self) -> str:
        """
        Calculate the nenewe day and Metke month based on the Metke value.

        Returns:
            Tuple[int, int]: The nenewe day and Metke month.
        """
        nenewe_day, metke_month = self.get_nenewe_date()
        metke = self.get_metke()
        first_day = self.get_first_day_of_year()
        day_of_metke = add_days(first_day, metke_month + metke - 1)
        day_of_nenewe = getattr(EletTewsak, day_of_metke)

        
        return (
            f"Tir {nenewe_day}"
            if day_of_nenewe + metke <= 30 and metke_month == 0
            else f"Yekatit {nenewe_day}"
            )

    def get_event_date(self, event_name: str) -> str:
        """
        Calculate the date of an event based on the nenewe day and the length to the event.

        Args:
            event_name (str): The name of the event.

        Returns:
            str: The date of the event.
        """

        total_years = self.get_total_years()
        metke = self.get_metke()
        nenewe_day, metke_month = self.get_nenewe_date()

        # Total days from all years including B.C and A.D
        total_days = get_total_days(total_years)
        # Total days from all years including B.C and A.D till the metke of the year
        total_days_till_metke = total_days + metke_month + metke

        day_of_week_of_metke = get_day_of_week(total_days_till_metke)
        # Getting the Twesak of each event
        nenewe_to_event_length = getattr(FastStartingDays(), event_name)

        days_to_nenewe = calculate_days_to_nenewe(day_of_week_of_metke)
        month_of_event, day_of_event = calculate_event_date(
            total_days_till_metke, days_to_nenewe, nenewe_to_event_length, total_days
        )


        return f"{EthiopianCalendarMonths().reverse_mapping[month_of_event]} {day_of_event}"

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

    def get_wengelawyan(self) -> str:
        """
        Get the gospel of the year.

        Returns:
            str: The Gospel (Wengelawyan) of the year
        """
        gospels = self._given_year % 4
        return Wengelawyan().reverse_mapping[gospels]

    def get_awde_kemer(self) -> Tuple[int, int, int]:
        """
        Get the awde kemer.

        Returns:
            int: the ith awde kemer we are at (based on the given year)
            int: the past years in the awde kemer
            int: the years left for the awde kemer to finish
        """
        total_years = self.get_total_years()
        ith_abiy_kemer = (total_years // self._abiy_kemer) + 1
        passed_years = total_years % self._abiy_kemer
        reminded_years = self._abiy_kemer - passed_years
        # print(f"""We are in the {ith_abiy_kemer}th Abiy kemer \n 
        #       have gone through {passed_years} years \n
        #       and have {reminded_years} years left""")
        return ith_abiy_kemer, passed_years, reminded_years

    def get_awde_mahtot(self) -> Tuple[int, int, int]:
        """
        Get the awde mahtot.

        Returns:
            int: the ith awde mahtot we are at (based on the given year)
            int: the past years in the awde mahtot
            int: the years left for the awde mahtot to finish
        """
        total_years = self.get_total_years()
        ith_awde_mahtot = (total_years // self._awde_mahtot) + 1
        passed_years = total_years % self._awde_mahtot
        reminded_years = self._awde_mahtot - passed_years
        # print(f"""We are in the {ith_awde_mahtot}th Awde Mahtot \n 
        #       have gone through {passed_years} years \n
        #       and have {reminded_years} years left""")
        return ith_awde_mahtot, passed_years, reminded_years

    def get_awde_tsehay(self) -> Tuple[int, int, int]:
        """
        Get the awde tsehay.

        Returns:
            int: the ith awde tsehay we are at (based on the given year)
            int: the past years in the awde tsehay
            int: the years left for the awde tsehay to finish
        """
        total_years = self.get_total_years()
        ith_awde_tsehay = (total_years // self._awde_tsehay) + 1
        passed_years = total_years % self._awde_tsehay
        reminded_years = self._awde_tsehay - passed_years
        # print(f"""We are in the {ith_awde_tsehay}th Awde Mahtot \n 
        #       have gone through {passed_years} years \n
        #       and have {reminded_years} years left""")
        return ith_awde_tsehay, passed_years, reminded_years

    def ethiopian_to_gregorian(
        self, ethiopian_year: int, ethiopian_month: int, ethiopian_day: int
    ) -> Tuple[int, int, int]:
        """Convert an Ethiopian date to a Gregorian date.

        Args:
            ethiopian_year (int): The Ethiopian year.
            ethiopian_month (int): The Ethiopian month.
            ethiopian_day (int): The Ethiopian day.

        Returns:
            Tuple[int, int, int]: The Gregorian year, month, and day.
        """

        return calculate_ethiopian_to_gregorian(
            ethiopian_year, ethiopian_month, ethiopian_day
        )

    def gregorian_to_ethiopian(
        self, gregorian_year: int, gregorian_month: int, gregorian_day: int
    ) -> Tuple[int, int, int]:
        """Convert a Gregorian date to an Ethiopian date.

        Args:
            gregorian_year (int): The Gregorian year.
            gregorian_month (int): The Gregorian month.
            gregorian_day (int): The Gregorian day.

        Returns:
            Tuple[int, int, int]: The Ethiopian year, month, and day.
        """
        return calculate_gregorian_to_ethiopian(
            gregorian_year, gregorian_month, gregorian_day
        )
