# BaherHasab Class

The `BaherHasab` class is used to perform calculations related to the Ethiopian calendar, specifically for calculating the total years since the creation of the world, the Wember value, and the Abketa value.

## Initialization

### `__init__(self, given_year: int = 2016) -> None`

Initializes the `BaherHasab` class with the given current year.

#### Args:
- `given_year` (int): The current year in the Ethiopian calendar (7 or 8 years less than the Gregorian calendar depending on the season of the year).

#### Example:
```python
baher_hasab = BaherHasab(given_year=2016)
```


## Baher haseb Methods
### `get_total_years(self) -> int`
Calculates the total years since the creation of the world according to the Ethiopian calendar.

#### Returns:
int: The total number of years.

#### Example:
```python
total_years = baher_hasab.get_total_years()
print(total_years)  # Outputs 7516
```


### `get_wember(self) -> int`
Calculates the Wember value for the current year. (We subtract one because the year has started, not finished).

#### Returns:
int: The Wember value.

#### Example:
```python
wember = baher_hasab.get_wember()
print(wember)  # Outputs '6'
```


### `get_abketa(self) -> int`
Calculates the Abketa value based on the Wember value.

#### Returns:
int: The Abketa value.

#### Example:
```python
abketa = baher_hasab.get_abketa()
print(abketa)  # Outputs '13'
```


### `get_metke(self) -> int`
Calculates the Metke value based on the Abketa value.

#### Returns:
int: The Metke value.

#### Example:
```python
metke = baher_hasab.get_metke()
print(metke)  # Outputs the Metke value 17
```


### `get_first_day_of_year(self) -> str`
Calculates the first day of the year according to the Ethiopian calendar.

#### Returns:
str: The first day of the year

#### Example:
```python
first_day = baher_hasab.get_first_day_of_year()
print(first_day)  # Outputs 'Wednesday'
```


### `get_nenewe(self) -> Tuple[int, int]`
Calculates the nenewe date and Metke month based on the Metke value.

#### Returns:
int: The Day of the Nenewe Fast of the year
int: The Month of the mekte (0 if it is the first month, 30 if it is the second month)

#### Example:
```python
date, metke_month = baher_hasab.get_nenewe()
print(date, metke_month)  # Outputs 9 30
```


### `get_event_date(self, event_name: str) -> str`
Calculates the date of an event based on the nenewe date and the length to the event.

#### Args:
str: event of the year. it has to be from the following ones
- hudade
- debrezeit
- hosana
- seklet
- tensae
- rekeb_kanat
- erget 
- piraklitos
- hawaryat
- dehenet

#### Returns:
str: The Date of the Event

#### Example:
```python
date = baher_hasab.get_event_date('hudade')
print(date)  # Outputs Tir 30
```

### `get_wengelawyan(self) -> str`
Get the gospel of the year

#### Returns:
str: The Gospel of the year. It has to be one of 
- Matthew
- Luke
- Mark
- John

#### Example:
```python
gospel = baher_hasab.get_wengelawyan()
print(gospel)  # Outputs John
```


### `get_awde_kemer(self) -> Tuple[int, int, int]:`
Gets the awde kemer of the year. In other other words on which year we are in the 532 cycle

#### Returns:
int: the ith awde kemer we are at (based on the given year)
int: the past years in the awde kemer 
int: the years left for the awde kemer to finish

#### Example:
```python
ith_awde_kemer, past_years, left_years = baher_hasab.get_awde_kemer()
print(ith_awde_kemer, past_years, left_years)  # Outputs 14, 332, 200
```


### `get_awde_mahtot(self) -> Tuple[int, int, int]:`
Gets the Awde Mahtot of the year. In other other words on which year we are in the 76 cycle

#### Returns:
int: the ith awde mahtot we are at (based on the given year)
int: the past years in the awde mahtot 
int: the years left for the awde mahtot to finish

#### Example:
```python
ith_awde_mahtot, past_years, left_years = baher_hasab.get_awde_mahtot()
print(ith_awde_mahtot, past_years, left_years)  # Outputs 30, 40, 36
```


### `get_awde_tsehay(self) -> Tuple[int, int, int]:`
Gets the awde tsehay of the year. In other other words on which year we are in the 28 cycle

#### Returns:
int: the ith awde tsehay we are at (based on the given year)
int: the past years in the awde tsehay 
int: the years left for the awde tsehay to finish

#### Example:
```python
ith_awde_tsehay, past_years, left_years = baher_hasab.get_awde_tsehay()
print(ith_awde_tsehay, past_years, left_years)  # Outputs 140, 18, 10
```

## Calendar Converter Methods
### `ethiopian_to_gregorian(ethiopian_year: int, ethiopian_month: int, ethiopian_day: int) -> tuple[int, int, int]:`
Convert an Ethiopian date to a Gregorian date.

### Args:
ethiopian_year (int): The Ethiopian year.
ethiopian_month (int): The Ethiopian month.
ethiopian_day (int): The Ethiopian day.

# Returns:
Tuple[int, int, int]: The Gregorian year, month, and day.


#### Example:
```python
gregorian_year, gregorian_month, gregorian_day = baher_hasab.ethiopian_to_gregorian(2016, 11, 18)
print(gregorian_year, gregorian_month, gregorian_day)  # Outputs 2024, 7, 25
```

### `gregorian_to_ethiopian(gregorian_year: int, gregorian_month: int, gregorian_day: int) -> tuple[int, int, int]:`
Convert a Gregorian date to an Ethiopian date.

#### Args:
gregorian_year (int): The Gregorian year.
gregorian_month (int): The Gregorian month.
gregorian_day (int): The Gregorian day.

#### Returns:
Tuple[int, int, int]: The Ethiopian year, month, and day.


#### Example:
```python
ethiopian_year, ethiopian_month, ethiopian_day = baher_hasab.gregorian_to_ethiopian(2024, 7, 25)
print(ethiopian_year, ethiopian_month, ethiopian_day)  # Outputs 2016, 11, 18
```




## Attributes
##### abiy_kemer
- Value: 532
- Description: Also known as abiy awde.
##### awde_mahtot
- Value: 76
- Description: Also known as mahkelawi awde.
##### awde_tsehay
- Value: 28
- Description: Also known as nuhase awde.
##### awde_abketa
- Value: 19
##### old_abketa
- Value: 11
##### amet_alem
- Value: 5500
- Description: Years before Christ
##### given_year
- Value: The given year passed during initialization.