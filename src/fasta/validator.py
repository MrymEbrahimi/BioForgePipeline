def validate_dna(sequence):
    """Validate a DNA sequence.

    A valid DNA sequence contains only the nucleotides A, T, C, and G.
    Invalid characters are not removed or corrected.

    Args:
        sequence: DNA sequence to validate.

    Raises:
        InvalidSequenceError: If the sequence contains an invalid character.
    """