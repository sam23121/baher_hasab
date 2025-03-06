# Baher Hasab (ባህረ ሃሳብ) 🇪🇹 

## Overview

Ethiopia has its own ancient calendar based on the system called Baher Hasab - ባሕረ ሃሳብ which means the Sea of Ideas. Baher Hasab  also known as Abushakir is a chronological system used for calculating the times of festivals and the beginning and ending of the fasting days throughout the year.

The baher_hasab is a Python package that simplifies the process of working with the Baher Hasab (also known as Abushakir) calendar. This package provides a set of tools and functions to help users easily calculate the dates of festivals and the beginning and ending of fasting days throughout the year.


## Links
- [Documentation](https://sam23121.github.io/baher_hasab/baherhasab/)
- [Github](https://github.com/sam23121/baher_hasab)
- [PyPI](https://pypi.org/project/baher_hasab/)
- [Issues](https://github.com/sam23121/baher_hasab/issues)
- [Extra Information](https://eotcmk.org/a/%E1%89%A3%E1%88%95%E1%88%A8-%E1%88%80%E1%88%B3%E1%89%A5/)


## Key Features

- **Calendar Conversion**: Easily convert between the Gregorian calendar and the Ethiopian calendar.
- **Festival Calculations**: Automatically determine the dates of major festivals and holidays based on the Baher Hasab calculations.
- **Fasting Day Tracking**: Effortlessly track the start and end dates of fasting periods throughout the year.

## Installation

To install the package, you can use `pip`:
```
pip install baher_hasab
```

## Usage

Here's a simple example of how to use the package:

```python
from baher_hasab import BaherHasab

# Create a Bahire Hasab instance
bh = BaherHasab(given_year=2016)

# Get the date of a specific festival
event_date = bh.get_event_date('hudade')
print(event_date) # Outputs Megabit 2
```

## Contribution
Contributions to the baher_hasab package are welcome! If you encounter any issues or have suggestions for new features, please feel free to open an issue or submit a pull request on the GitHub repository.

## Note
Defining some terms to get started:
- **Baher Hasab**: Also known as Abushakir, is a chronological system used for calculating the times of festivals and the beginning and ending of the fasting days throughout the year.
- **neneweh** (ነነዌ): is the Ethiopian name for The three day fast that the neneweh people did (Book of Jonah)
- **Hudade** (ሁዳዴ): also known as abiy_tsome (አብይ ጾም) is the Ethiopian name for the Great Lent.
- **debrezeit** (ደብረዘይት): is the Ethiopian name for the middle day of the Great lent.
- **hosana** (ሆሳዕና): is the Ethiopian name for the day of Entrance of Jesus to Jerusalem.
- **seklet** (ስቅለት): is the Ethiopian name for the holy Friday.
- **tensae** (ትንሳኤ): is the Ethiopian name for the Easter.
- **rekeb_kanat** (ርክበ ካህናት): is the Ethiopian name for the "Coming together of the priests".
- **erget** (ዕርገት): is the Ethiopian name for the day of ascension of Jesus Christ.
- **piraklitos** (ጰራቅሊጦስ): is the Ethiopian name for the Pentecost.
- **hawaryat** (ሐዋርያት): is the Ethiopian name for the fast of the apostles.
- **dehenet** (ድህንነት
): is the Ethiopian name for the starting day of wenesday and friday fasting.
- **wengelawyan** (ወንጌላውያን): is the Ethiopian name for the gospel of the year.
- **awde_kemer** (አውደ ቀመር): its a cycle that comes every 532 years.
- **awde_mahtot** (አውደ ማሕቶት): its a cycle that comes every 76 years.
- **awde_tsehay** (አውደ መስከር): its a cycle that comes every 28 years.





