from src.exceptions import DataFileError
def load_codon_table(path):
    codon_table = {}
    with open(path,"r") as file:
        for line_number,line in enumerate(file,start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                raise DataFileError(f"Invalid data at line {line_number}")
            codon, amino_acid = parts
            codon_table[codon] = amino_acid

    return codon_table
def load_amino_weight(path):
    amino_weights = {}
    with open(path,"r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                raise DataFileError(f"Invalid data at line {line_number}")
            amino_acid, weight = parts
            
            try:
                weight = float(weight)
            except ValueError:
                raise DataFileError(f"Invalid weight at line {line_number}")
            amino_weights[amino_acid] = weight
    return amino_weights
