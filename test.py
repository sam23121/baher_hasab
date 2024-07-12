import unittest
from baher_hasab import BaherHasab


class TestBaherHasab(unittest.TestCase):
    def setUp(self):
        """Set up any necessary data or state before each test."""
        self.year_current = BaherHasab(current_year=2016)
        self.year_random = BaherHasab(current_year=1962)
        self.year_lowest = BaherHasab(current_year=1972)
        self.year_highest = BaherHasab(current_year=1975)

    def test_get_total_years(self):
        result = self.year_random.get_total_years()
        expected = 7462  # 5500 + 1962
        self.assertEqual(result, expected, "Total years should be 7462")

        result = self.year_lowest.get_total_years()
        expected = 7472  # 5500 + 1962
        self.assertEqual(result, expected, "Total years should be 7472")

        result = self.year_highest.get_total_years()
        expected = 7475  # 5500 + 1962
        self.assertEqual(result, expected, "Total years should be 7475")

        result = self.year_current.get_total_years()
        expected = 7516  # 5500 + 1962
        self.assertEqual(result, expected, "Total years should be 7516")

    def test_get_wember(self):
        result = self.year_random.get_wember()
        expected = 13  # Calculation based on 5516
        self.assertEqual(result, expected, "Wember should be 13")

        result = self.year_lowest.get_wember()
        expected = 4  # Calculation based on 5516
        self.assertEqual(result, expected, "Wember should be 4")

        result = self.year_highest.get_wember()
        expected = 7  # Calculation based on 5516
        self.assertEqual(result, expected, "Wember should be 7")

        result = self.year_current.get_wember()
        expected = 10  # Calculation based on 5516
        self.assertEqual(result, expected, "Wember should be 10")

    def test_get_abketa(self):
        result = self.year_random.get_abketa()
        expected = 23  # Calculation based on Wember 0
        self.assertEqual(result, expected, "Abketa should be 23")

        result = self.year_lowest.get_abketa()
        expected = 14  # Calculation based on Wember 0
        self.assertEqual(result, expected, "Abketa should be 14")

        result = self.year_highest.get_abketa()
        expected = 17  # Calculation based on Wember 0
        self.assertEqual(result, expected, "Abketa should be 17")

        result = self.year_current.get_abketa()
        expected = 20  # Calculation based on Wember 0
        self.assertEqual(result, expected, "Abketa should be 20")

    def test_get_metke(self):
        result = self.year_random.get_metke()
        expected = 7  # Calculation based on Abketa 0
        self.assertEqual(result, expected, "Metke should be 7")

        result = self.year_lowest.get_metke()
        expected = 16  # Calculation based on Abketa 0
        self.assertEqual(result, expected, "Metke should be 16")

        result = self.year_highest.get_metke()
        expected = 13  # Calculation based on Abketa 0
        self.assertEqual(result, expected, "Metke should be 13")

        result = self.year_current.get_metke()
        expected = 10  # Calculation based on Abketa 0
        self.assertEqual(result, expected, "Metke should be 10")

    def test_get_first_day_of_year(self):
        result = self.year_random.get_first_day_of_year()
        expected = "thursday"  # Calculation based on 5516 total years
        self.assertEqual(result, expected, "First day of year should be 'thursday'")

        result = self.year_lowest.get_first_day_of_year()
        expected = "wednesday"  # Calculation based on 5516 total years
        self.assertEqual(result, expected, "First day of year should be 'wednesday'")

        result = self.year_highest.get_first_day_of_year()
        expected = "saturday"  # Calculation based on 5516 total years
        self.assertEqual(result, expected, "First day of year should be 'saturday'")

        result = self.year_current.get_first_day_of_year()
        expected = "tuesday"  # Calculation based on 5516 total years
        self.assertEqual(result, expected, "First day of year should be 'tuesday'")

    def test_add_days(self):
        result = self.year_random.add_days("thursday", 36)
        expected = "friday"
        self.assertEqual(
            result, expected, "Adding 37 days to 'thursday' should give 'friday'"
        )

        # result = self.year_lowest.add_days('thursday', 36)
        # expected = 'friday'
        # self.assertEqual(result, expected, "Adding 37 days to 'thursday' should give 'friday'")

        # result = self.year_highest.add_days('thursday', 36)
        # expected = 'friday'
        # self.assertEqual(result, expected, "Adding 37 days to 'thursday' should give 'friday'")

        # result = self.year_current.add_days('thursday', 36)
        # expected = 'friday'
        # self.assertEqual(result, expected, "Adding 37 days to 'thursday' should give 'friday'")

    def test_get_nenewa(self):
        # EletTewsak.sunday = 7  # Example value
        result, metke_month = self.year_random.get_nenewa()
        expected_result = 9  # Based on the calculation and example data
        self.assertEqual(result, expected_result, "Nenewa day should be 9")
        self.assertEqual(metke_month, 30, "Metke month should be 30")

        result, metke_month = self.year_lowest.get_nenewa()
        expected_result = 19  # Based on the calculation and example data
        self.assertEqual(result, expected_result, "Nenewa day should be 19")
        self.assertEqual(metke_month, 0, "Metke month should be 0")

        result, metke_month = self.year_highest.get_nenewa()
        expected_result = 21  # Based on the calculation and example data
        self.assertEqual(result, expected_result, "Nenewa day should be 21")
        self.assertEqual(metke_month, 30, "Metke month should be 30")

        result, metke_month = self.year_current.get_nenewa()
        expected_result = 18  # Based on the calculation and example data
        self.assertEqual(result, expected_result, "Nenewa day should be 18")
        self.assertEqual(metke_month, 30, "Metke month should be 30")

    def test_get_hudade(self):
        result = self.year_random.get_hudade()
        expected = "Yekatit 23"
        self.assertEqual(result, expected, "Hudade fast should be on 'Yekatit 23'")

        result = self.year_lowest.get_hudade()
        expected = "Yekatit 3"
        self.assertEqual(result, expected, "Hudade fast should be on 'Yekatit 3'")

        result = self.year_highest.get_hudade()
        expected = "Megabit 5"
        self.assertEqual(result, expected, "Hudade fast should be on 'Megabit 5'")

        result = self.year_current.get_hudade()
        expected = "Megabit 2"
        self.assertEqual(result, expected, "Hudade fast should be on 'Megabit 2'")

    def test_get_debrezeit(self):
        result = self.year_random.get_debrezeit()
        expected = "Megabit 20"
        self.assertEqual(result, expected, "Debrezeit should be on 'Megabit 20'")

        result = self.year_lowest.get_debrezeit()
        expected = "Yekatit 30"
        self.assertEqual(result, expected, "Debrezeit should be on 'Yekatit 30'")

        result = self.year_highest.get_debrezeit()
        expected = "Miyazia 2"
        self.assertEqual(result, expected, "Debrezeit should be on 'Miyazia 2'")

        result = self.year_current.get_debrezeit()
        expected = "Megabit 29"
        self.assertEqual(result, expected, "Debrezeit should be on 'Megabit 29'")

    def test_get_hosana(self):
        result = self.year_random.get_hosana()
        expected = "Miyazia 11"
        self.assertEqual(result, expected, "Hosana should be on 'Miyazia 11'")

        result = self.year_lowest.get_hosana()
        expected = "Megabit 21"
        self.assertEqual(result, expected, "Hosana should be on 'Megabit 21'")

        result = self.year_highest.get_hosana()
        expected = "Miyazia 23"
        self.assertEqual(result, expected, "Hosana should be on 'Miyazia 23'")

        result = self.year_current.get_hosana()
        expected = "Miyazia 20"
        self.assertEqual(result, expected, "Hosana should be on 'Miyazia 20'")

    def test_get_seklet(self):
        result = self.year_random.get_seklet()
        expected = "Miyazia 16"
        self.assertEqual(result, expected, "Seklet should be on 'Miyazia 16'")

        result = self.year_lowest.get_seklet()
        expected = "Megabit 26"
        self.assertEqual(result, expected, "Seklet should be on 'Megabit 26'")

        result = self.year_highest.get_seklet()
        expected = "Miyazia 28"
        self.assertEqual(result, expected, "Seklet should be on 'Miyazia 28'")

        result = self.year_current.get_seklet()
        expected = "Miyazia 25"
        self.assertEqual(result, expected, "Seklet should be on 'Miyazia 25'")

    def test_get_tensae(self):
        result = self.year_random.get_tensae()
        expected = "Miyazia 18"
        self.assertEqual(result, expected, "Tensae should be on 'Miyazia 18'")

        result = self.year_lowest.get_tensae()
        expected = "Megabit 28"
        self.assertEqual(result, expected, "Tensae should be on 'Megabit 28'")

        result = self.year_highest.get_tensae()
        expected = "Miyazia 30"
        self.assertEqual(result, expected, "Tensae should be on 'Miyazia 30'")

        result = self.year_current.get_tensae()
        expected = "Miyazia 27"
        self.assertEqual(result, expected, "Tensae should be on 'Miyazia 27'")

    def test_get_rekeb_kanat(self):
        result = self.year_random.get_rekeb_kanat()
        expected = "Genbot 12"
        self.assertEqual(result, expected, "Rekeb Kanat should be on 'Genbot 12'")

        result = self.year_lowest.get_rekeb_kanat()
        expected = "Miyazia 22"
        self.assertEqual(result, expected, "Rekeb Kanat should be on 'Miyazia 22'")

        result = self.year_highest.get_rekeb_kanat()
        expected = "Genbot 24"
        self.assertEqual(result, expected, "Rekeb Kanat should be on 'Genbot 24'")

        result = self.year_current.get_rekeb_kanat()
        expected = "Genbot 21"
        self.assertEqual(result, expected, "Rekeb Kanat should be on 'Genbot 21'")

    def test_get_erget(self):
        result = self.year_random.get_erget()
        expected = "Genbot 27"
        self.assertEqual(result, expected, "Erget should be on 'Genbot 27'")

        result = self.year_lowest.get_erget()
        expected = "Genbot 7"
        self.assertEqual(result, expected, "Erget should be on 'Genbot 7'")

        result = self.year_highest.get_erget()
        expected = "Sene 9"
        self.assertEqual(result, expected, "Erget should be on 'Sene 9'")

        result = self.year_current.get_erget()
        expected = "Sene 6"
        self.assertEqual(result, expected, "Erget should be on 'Sene 6'")

    def test_get_piraklitos(self):
        result = self.year_random.get_piraklitos()
        expected = "Sene 7"
        self.assertEqual(result, expected, "Piraklitos fast should be on 'Sene 7'")

        result = self.year_lowest.get_piraklitos()
        expected = "Genbot 17"
        self.assertEqual(result, expected, "Piraklitos fast should be on 'Genbot 17'")

        result = self.year_highest.get_piraklitos()
        expected = "Sene 19"
        self.assertEqual(result, expected, "Piraklitos fast should be on 'Sene 19'")

        result = self.year_current.get_piraklitos()
        expected = "Sene 16"
        self.assertEqual(result, expected, "Piraklitos fast should be on 'Sene 16'")

    def test_get_hawaryat(self):
        result = self.year_random.get_hawaryat()
        expected = "Sene 8"
        self.assertEqual(result, expected, "Sene Fast fast should be on 'Sene 8'")

        result = self.year_lowest.get_hawaryat()
        expected = "Genbot 18"
        self.assertEqual(result, expected, "Sene Fast fast should be on 'Genbot 18'")

        result = self.year_highest.get_hawaryat()
        expected = "Sene 20"
        self.assertEqual(result, expected, "Sene Fast fast should be on 'Sene 20'")

        result = self.year_current.get_hawaryat()
        expected = "Sene 17"
        self.assertEqual(result, expected, "Sene Fast fast should be on 'Sene 17'")

    def test_get_dehenet(self):
        result = self.year_random.get_dehenet()
        expected = "Sene 10"
        self.assertEqual(result, expected, "Dehenet Fast fast should be on 'Sene 10'")

        result = self.year_lowest.get_dehenet()
        expected = "Genbot 20"
        self.assertEqual(result, expected, "Dehenet Fast fast should be on 'Sene 20'")

        result = self.year_highest.get_dehenet()
        expected = "Sene 22"
        self.assertEqual(result, expected, "Dehenet Fast fast should be on 'Sene 22'")

        result = self.year_current.get_dehenet()
        expected = "Sene 19"
        self.assertEqual(result, expected, "Dehenet Fast fast should be on 'Sene 19'")

    # def test_get_length_between(self):
    #     # FastStartingDays.hudade = 55  # Example value
    #     # nenewa = 7  # Example nenewa day
    #     result, day = self.year_random.get_length_between(nenewa, 'hudade')
    #     expected_length = 62  # Example calculation
    #     expected_day = 2  # Example calculation
    #     self.assertEqual(result, expected_length, "Length to event should be 62")
    #     self.assertEqual(day, expected_day, "Event day should be 2")

    # def test_get_event_date(self):
    #     MonthForFasting.hudade = {'Tir': 14, 'Yekatit': 20}  # Example values
    #     result = self.year_random.get_event_date('hudade')
    #     expected = 'Tir 2'  # Example calculation
    #     self.assertEqual(result, expected, "Event date should be 'Tir 2'")


if __name__ == "__main__":
    unittest.main()
