from dataclasses import dataclass, asdict, field
from typing import Dict


class ReverseMapping:
    """Class to provide reverse mapping functionality."""

    @property
    def reverse_mapping(self) -> Dict[int, str]:
        """Create a reverse mapping of the days."""
        return {v: k for k, v in asdict(self).items()}


@dataclass(frozen=True)
class DaysBookmark(ReverseMapping):
    monday: int = 0
    tuesday: int = 1
    wednesday: int = 2
    thursday: int = 3
    friday: int = 4
    saturday: int = 5
    sunday: int = 6


@dataclass(frozen=True)
class EletTewsak(ReverseMapping):
    saturday: int = 8
    sunday: int = 7
    monday: int = 6
    tuesday: int = 5
    wednesday: int = 4
    thursday: int = 3
    friday: int = 2


@dataclass(frozen=True)
class FastStartingDays:
    hudade: int = 14
    debrezeit: int = 41  # 11
    hosana: int = 62  # 2
    seklet: int = 67  # 7
    tensae: int = 69  # 9
    rekeb_kanat: int = 93  # 3
    erget: int = 108  # 18
    piraklitos: int = 118  # 28
    hawaryat: int = 119  # 29
    dehenet: int = 121  # 1


@dataclass(frozen=True)
class MonthForFasting:
    hudade: Dict[str, int] = field(
        default_factory=lambda: {"Yekatit": 30, "Megabit": 60}
    )  # 6 7
    debrezeit: Dict[str, int] = field(
        default_factory=lambda: {"Yekatit": 30, "Megabit": 60, "Miyazia": 90}
    )  # x 6 7 8
    hosana: Dict[str, int] = field(
        default_factory=lambda: {"Megabit": 60, "Miyazia": 90}
    )  # 7 8
    seklet: Dict[str, int] = field(
        default_factory=lambda: {"Megabit": 60, "Miyazia": 90}
    )  # 7 8
    tensae: Dict[str, int] = field(
        default_factory=lambda: {"Megabit": 60, "Miyazia": 90}
    )  # 7 8
    rekeb_kanat: Dict[str, int] = field(
        default_factory=lambda: {"Miyazia": 90, "Genbot": 120}
    )  # 8 9
    erget: Dict[str, int] = field(
        default_factory=lambda: {"Genbot": 120, "Sene": 150}
    )  # 9 10
    piraklitos: Dict[str, int] = field(
        default_factory=lambda: {"Genbot": 120, "Sene": 150}
    )  # 9 10
    hawaryat: Dict[str, int] = field(
        default_factory=lambda: {"Genbot": 120, "Sene": 150}
    )  # 9 10
    dehenet: Dict[str, int] = field(
        default_factory=lambda: {"Genbot": 120, "Sene": 150}
    )  # 9 10
