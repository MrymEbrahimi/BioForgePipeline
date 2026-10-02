import re

from exceptions import InvalidSequenceError


def validate_sequence(sequence):
    if not re.fullmatch(r"[ACGT]+", sequence):
        raise InvalidSequenceError("Invalid DNA sequence")
    