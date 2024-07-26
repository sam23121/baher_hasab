# About 

## Overview

Ethiopia has its own ancient calendar based on the system called Baher Hasab - ባሕረ ሃሳብ which means the Sea of Ideas. Baher Hasab  also known as Abushakir is a chronological system used for calculating the times of festivals and the beginning and ending of the fasting days throughout the year.

The baher_hasab is a Python package that simplifies the process of working with the Baher Hasab (also known as Abushakir) calendar. This package provides a set of tools and functions to help users easily calculate the dates of festivals and the beginning and ending of fasting days throughout the year.

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