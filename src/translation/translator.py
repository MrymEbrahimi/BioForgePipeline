def translate(codons, codon_table):
    """Translate codons into a protein sequence.

    Translation stops when a stop codon is encountered.

    Args:
        codons: Codons to translate.
        codon_table: Dictionary mapping codons to amino acids.

    Returns:
        A Protein object containing the translated sequence.
    """