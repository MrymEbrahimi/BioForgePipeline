
    
# Parsing
# Validation
# ORF Detection
# Translation

codon_table = {
    "AUG" : "M",
    "CUU" : "L",
    "UCA" : "S",
    "UUC" : "F",
    "UGA" : "STOP",
    "UAA" : "STOP",
    "UAG" : "STOP",
}
def translate(RNA):
    protein = ""
    if len(RNA) % 3 != 0:
        raise ValueError("RNA length must be a multiple of 3")
    for i in range(0,len(RNA),3):
        codon = RNA[i:i+3]
        if codon in ["UAA","UAG","UGA"]:
            break
        if codon not in codon_table:
            raise   ValueError("Invalid codon")
        amino_acid = codon_table[codon]
        protein += amino_acid
    return protein
RNA = ""
print(translate(RNA))
# Filtering
# Annotation
# Reporting
# Logging
