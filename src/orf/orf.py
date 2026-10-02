<<<<<<< HEAD
def test():
    print("Maryam & Mohammad")
=======
class ORF:
    def __init__(self,strand,frame: int,start_pos:int,protein:str,is_complete: bool) -> None:
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.protein = protein
        self.is_complete = is_complete
    """Represent an Open Reading Frame (ORF).

    Attributes:
        strand: DNA strand where the ORF was found.
        frame: Reading frame of the ORF.
        start_pos: Start position of the ORF in the original DNA sequence.
        protein: Protein sequence translated from the ORF.
        is_complete: Indicates whether the ORF has a valid stop codon.
    """
>>>>>>> main
