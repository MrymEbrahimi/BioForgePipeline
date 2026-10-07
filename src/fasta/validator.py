import re

from src.exceptions import InvalidSequenceError


def validate_dna(sequence):
    """Validate a DNA sequence.

    A valid DNA sequence contains only A, T, C, and G.
    Invalid characters are not removed or corrected.
    """

    if not sequence:
        raise InvalidSequenceError("DNA sequence cannot be empty")

    # Check that the entire sequence contains only valid DNA bases.
    if not re.fullmatch(r"[ATCG]+", sequence.upper()):
        raise InvalidSequenceError(
            f"Invalid DNA sequence: {sequence}"
        )
