from src.exceptions import DataFileError
def load_codon_table(path):
    codon_table = {}
    with open(path,"r") as file:
        lines = file.readlines()
    for line_number,line in enumerate(lines,start=1):
        parts = line.strip().split()
        if len(parts) != 3:
            raise DataFileError(f"Invalid data at line {line_number}")
        codon_table[parts[0]] = parts[1]
    return codon_table
def load_amino_weight(path):
    amino_weights = {}
    with open(path,"r") as file:
        lines = file.readlines()
    for line_number,line in enumerate(lines,start=1):
        parts = line.strip().split()
        if len(parts) != 2:
            raise DataFileError(f"Invalid data at line {line_number}")
        amino_weights[parts[0]] = float(parts[1])
    return amino_weights
