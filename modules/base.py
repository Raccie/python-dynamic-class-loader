from enum import Enum

class Family(Enum):
    MAMMAL = 0
    FISH = 1
    AMPHIBIAN = 2
    REPTILE = 3
    BIRD = 4
    INVERTIBRATES = 5

class Species:
    def __init__(self, name, family):
        self._name = name
        self._family = family

    def __str__(self):
        return F"{self._name} is classified as {self._family}"
