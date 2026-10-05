from protein import protein

def translate(codons, codon_table):
    sequence = ""
    for codon in codons:
        if codon not in codon_table:
            raise ValueError(f"Unknown codon: {codon}")
        amino_acid = codon_table[codon]

        if amino_acid == "*":
            break
        sequence += amino_acid
    return protein(sequence)


# Filtering
# Annotation
# Reporting
# Logging


