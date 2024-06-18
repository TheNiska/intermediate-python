from collections.abc import Sequence, Iterable, Hashable
from random import shuffle
from typing import TypeVar
from decimal import Decimal
from fractions import Fraction

T = TypeVar('T')
NumberT = TypeVar('NumberT', float, Decimal, Fraction)
HashableT = TypeVar('HashableT', bound=Hashable)

def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')

    result = list(population)
    shuffle(result)
    return result[:size]

def mode(data: Iterable[NumberT]) -> NumberT:
    pass


def mode(data: Iterable[HashableT]) -> HashableT:
    pass



