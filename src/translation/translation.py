from .protein import Protein

def translate(rna, codon_table):
    sequence = ""
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if codon not in codon_table:
            continue
        amino_acid = codon_table[codon]
        if amino_acid == "*" or amino_acid == "STOP":
            break
        sequence += amino_acid
    return Protein(sequence)
