from src.exceptions import InvalidSequenceError
import re
def validate_dna(sequence):
    """Validate a DNA sequence.

    A valid DNA sequence contains only the nucleotides A, T, C, and G.
    Invalid characters are not removed or corrected.

    Args:
        sequence: DNA sequence to validate.

    Raises:
        InvalidSequenceError: If the sequence contains an invalid character.
    """
    if not sequence:
        raise InvalidSequenceError("DNA sequence cannot be empty")

    if not re.fullmatch(r"[ATCG]+", sequence.upper()):
        raise InvalidSequenceError(
            f"Invalid DNA sequence: {sequence}"
        )