from baher_hasab.lookups import DaysBookmark, EletTewsak, FastStartingDays, MonthForFasting, Wengelawyan, EthiopianCalendarMonths
from typing import Tuple


class BaherHasab:
    def __init__(self, given_year: int = 2016) -> None:
        """
        Initialize the BaherHasab class with the given current year.

        Args:
            given_year (int): The current year in the Ethiopian calendar (its 7 or 8 years less than the 
                                    Geogorian calendar depending on the season of the year).
        """
        self.abiy_kemer = 532  # also known as abiy awde
        self.awde_mahtot = 76  # also known as mahkelawi awde
        self.awde_tsehay = 28  # also known as nuhase awde
        self.awde_abketa = 19
        self.old_abketa = 11
        self.amet_alem = 5500
        self.given_year = given_year

    def get_total_years(self) -> int:
        """
        Calculate the total years since the creation of the world according to the Ethiopian calendar.

        Returns:
            int: The total number of years.
        """
        return self.amet_alem + self.given_year

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

    def get_nenewe(self) -> Tuple[int, int]:
        """
        Calculate the nenewe day and Metke month based on the Metke value.

        Returns:
            Tuple[int, int]: The nenewe day and Metke month.
        """
        metke = self.get_metke()
        print('Metke', metke)
        metke_month = 0 if metke > 13 else 30
        first_day = self.get_first_day_of_year()
        print("first day", first_day)
        day_of_metke = self.add_days(first_day, metke_month + metke - 1)
        print("day_of_metke", day_of_metke)

        day_of_nenewe = getattr(EletTewsak, day_of_metke)
        print("day_of_nenewe", day_of_nenewe)

        nenewe_day = (metke_month + metke + day_of_nenewe) % 30
        print("nenewe_day", nenewe_day)

        print(f"Tir {nenewe_day}" if day_of_nenewe + metke <= 30 and metke_month == 0 else f"Yekatit {nenewe_day}")

        return nenewe_day, metke_month

    def get_length_between(self, nenewe: int, fast: str) -> Tuple[int, int]:
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

    # def get_event_date(self, event_name: str) -> str:
    #     """
    #     Calculate the date of an event based on the nenewe day and the length to the event.

    #     Args:
    #         event_name (str): The name of the event.

    #     Returns:
    #         str: The date of the event.
    #     """
    #     nenewe, metke_month = self.get_nenewe()
    #     length_to_event, day_of_event = self.get_length_between(nenewe, event_name)

    #     months = MonthForFasting()
    #     months = getattr(months, event_name)

    #     # min_value = min(months.values())

    #     for month, value in months.items():
    #         if metke_month > 0:
    #             if length_to_event > value:
    #                 continue
    #         else:
    #             if length_to_event - 30 > value:
    #                 continue
    #         return f"{month} {day_of_event}"
        
    def get_event_date(self, event_name: str) -> str:
        """
        Calculate the date of an event based on the nenewe day and the length to the event.

        Args:
            event_name (str): The name of the event.

        Returns:
            str: The date of the event.
        """
        # Step 1-2
        total_years = self.get_total_years()
        # print("Step 2", total_years)
        

        # Step 3-6
        metke = self.get_metke()
        nenewe_day, metke_month = self.get_nenewe()
        # print("Step 5", metke)
        # print("Step 6", metke_month)


        # Step 7
        year_fractions = total_years // 4
        # print("Step 7", year_fractions)

        # total days from all years including B.C and A.D
        # Step 8
        total_days = (total_years-1)*365 + year_fractions
        # print("Step 8", total_days)

        months = FastStartingDays()
        tewsak_of_event = getattr(months, event_name)
        # print("tewsak", tewsak_of_event)


        # Total days from all years including B.C and A.D till the metke of the year
        # Step 10
        total_days_till_metke = total_days + metke_month + metke
        # print("Step 10", total_days_till_metke)

        # This is the day of the week where the metke will land given that year 
        # Step 11
        day_of_week_of_metke = (total_days_till_metke % 7) + 1
        # print("Step 11", day_of_week_of_metke)

        # this is the length of days from the metke to the start 
        # of nenewe fast (which is vital to the rest of events)
        # Step 12
        days_to_nenewe = 128 - ((day_of_week_of_metke+1)  % 7) + 1
        # print("Step 12", days_to_nenewe)

        # To find the tewsak of the event
        # Step 13
        day_of_event_starting_from_the_start = total_days_till_metke + days_to_nenewe + tewsak_of_event
        # print("Step 13", day_of_event_starting_from_the_start)


        # Month of the event
        # Step 14
        month_of_event = ((day_of_event_starting_from_the_start - total_days - 1) // 30) + 1
        if (day_of_event_starting_from_the_start - total_days - 1) // 30 == (day_of_event_starting_from_the_start - total_days - 1) / 30:
            month_of_event = (day_of_event_starting_from_the_start - total_days - 1) // 30
        # print("Step 14", month_of_event)

        # Step 15
        day_of_event = ((day_of_event_starting_from_the_start - total_days - 1) % 30)
        if day_of_event == 0:
            day_of_event = 30
        # print("Step 15", day_of_event)

        # Step 16
        day_of_week_event =  DaysBookmark().reverse_mapping[6 if (day_of_event_starting_from_the_start % 7) == 0 else (day_of_event_starting_from_the_start % 7) - 1]
        # print("Step 16", day_of_week_event)

        
        
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
        gospels = self.given_year % 4
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
        ith_abiy_kemer = (total_years // self.abiy_kemer) + 1
        passed_years = total_years % self.abiy_kemer
        reminded_years = self.abiy_kemer - passed_years
        print(f"""We are in the {ith_abiy_kemer}th Abiy kemer \n 
              have gone through {passed_years} years \n
              and have {reminded_years} years left""")
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
        ith_awde_mahtot = (total_years // self.awde_mahtot) + 1
        passed_years = total_years % self.awde_mahtot
        reminded_years = self.awde_mahtot - passed_years
        print(f"""We are in the {ith_awde_mahtot}th Awde Mahtot \n 
              have gone through {passed_years} years \n
              and have {reminded_years} years left""")
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
        ith_awde_tsehay = (total_years // self.awde_tsehay) + 1
        passed_years = total_years % self.awde_tsehay
        reminded_years = self.awde_tsehay - passed_years
        print(f"""We are in the {ith_awde_tsehay}th Awde Mahtot \n 
              have gone through {passed_years} years \n
              and have {reminded_years} years left""")
        return ith_awde_tsehay, passed_years, reminded_years
