"""
Generate random numbers for a lottery drawing.

Produces five unique numbers from 1 to 69 and one number from 1 to 26
using cryptographically secure randomness.
"""
from secrets import SystemRandom
from typing import List, Tuple

_rng = SystemRandom()


def generate_draw() -> Tuple[List[int], int]:
    """Return five distinct numbers 1-69 and one Powerball 1-26.

    Returns a tuple of the sorted five numbers and the single Powerball number.
    """
    main_numbers = _rng.sample(range(1, 70), k=5)
    powerball = _rng.randrange(1, 27)
    return sorted(main_numbers), powerball


def main() -> None:
    main_numbers, powerball = generate_draw()
    main_display = " ".join(f"{n:02d}" for n in main_numbers)
    print(f"Main numbers: {main_display}")
    print(f"Powerball: {powerball:02d}")


if __name__ == "__main__":
    main()
