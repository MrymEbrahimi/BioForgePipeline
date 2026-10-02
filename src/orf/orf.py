START_CODON = "ATG"
STOP_CODONS = {"TAA", "TAG", "TGA"}

class ORF:
    def __init__(self,strand: str,frame: int,start_pos:int,protein:str,is_complete: bool) -> None:
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.protein = protein
        self.is_complete = is_complete
 

