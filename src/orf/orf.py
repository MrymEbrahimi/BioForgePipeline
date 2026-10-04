from dataclasses import dataclass
START_CODON = "ATG"
STOP_CODONS = {"TAA", "TAG", "TGA"}
@dataclass
class ORF:
    strand: str
    frame: int
    start_pos: int
    protein: str
    is_complete: bool
    id: int|None = None
 

