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
    Monday: int = 0
    Tuesday: int = 1
    Wednesday: int = 2
    Thursday: int = 3
    Friday: int = 4
    Saturday: int = 5
    Sunday: int = 6


@dataclass(frozen=True)
class EletTewsak(ReverseMapping):
    Saturday: int = 8
    Sunday: int = 7
    Monday: int = 6
    Tuesday: int = 5
    Wednesday: int = 4
    Thursday: int = 3
    Friday: int = 2


@dataclass(frozen=True)
class Wengelawyan(ReverseMapping):
    Matthew: int = 1
    Mark: int = 2
    Luke: int = 3
    John: int = 0


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
class EthiopianCalendarMonths(ReverseMapping):
    Meskerem: int = 1
    Tikimt: int = 2
    Hidar: int = 3
    Tahsas: int = 4
    Tir: int = 5
    Yekatit: int = 6
    Megabit: int = 7
    Miyazia: int = 8
    Ginbot: int = 9
    Sene: int = 10
    Hamle: int = 11
    Nehasse: int = 12
    Pagumen: int = 13


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
        default_factory=lambda: {"Miyazia": 90, "Ginbot": 120}
    )  # 8 9
    erget: Dict[str, int] = field(
        default_factory=lambda: {"Ginbot": 120, "Sene": 150}
    )  # 9 10
    piraklitos: Dict[str, int] = field(
        default_factory=lambda: {"Ginbot": 120, "Sene": 150}
    )  # 9 10
    hawaryat: Dict[str, int] = field(
        default_factory=lambda: {"Ginbot": 120, "Sene": 150}
    )  # 9 10
    dehenet: Dict[str, int] = field(
        default_factory=lambda: {"Ginbot": 120, "Sene": 150}
    )  # 9 10
