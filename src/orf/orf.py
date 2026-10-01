class ORF:
    """Represent an Open Reading Frame (ORF).

    Attributes:
        strand: DNA strand where the ORF was found.
        frame: Reading frame of the ORF.
        start_pos: Start position of the ORF in the original DNA sequence.
        protein: Protein sequence translated from the ORF.
        is_complete: Indicates whether the ORF has a valid stop codon.
    """