import re
from .orf import ORF, START_CODON, STOP_CODONS

def find_orfs_reverse(dna: str):
    orfSeq = ""
    reverseComplement = convertDnaToReversComplemet(dna)
    start = findStartPos(reverseComplement)
    stop = findStop(reverseComplement) 
    if start == -1:
        return orfList
    
    
    if stop is None:
        orf = ORF(
            strand = "Reverse",
            frame = findFrames(dna),
            start_pos = len(dna) - start -1,
            protein = "",
            is_complete = False
        )
        orfSeq = reverseComplement[start:]
        return orfSeq
    else:
        orfSeq = reverseComplement[start:stop+3]
        orf = ORF(
            strand = "Reverse",
            frame = findFrames(dna),
            start_pos = len(dna) - start -1,
            protein = "",
            is_complete = True
        )
        orfList.append(orf)
    return orfList
        
def findStartPos(dna: str):
    for match in re.finditer("ATG",dna):
        start_pos = match.start()
        return start_pos
    return -1
    
def findFrames(dna:str):
    start = findStartPos(dna)
    if start is None:
        return 0
    return start % 3

def findStop(dna: str):
    start = findStartPos(dna)
    if start is None:
        return None
    pattern = r"TAA|TAG|TGA"
    for match in re.finditer(pattern, dna):
        if match.start() > start:
            return match.start()
    return None

def convertDnaToReversComplemet(dna: str):
    dna = dna.upper()
    reverse = dna[::-1]
    dnaTranslator = str.maketrans("ATCG","TAGC")
    reversComplement = reverse.translate(dnaTranslator)
    return reversComplement
    
    """Find Open Reading Frames on the reverse DNA strand.

    The function creates the reverse complement of the DNA sequence,
    checks all three reading frames, and converts ORF start positions
    back to their corresponding positions in the original DNA sequence.

    Args:
        dna: DNA sequence to analyze.

    Returns:
        A collection of ORFs found on the reverse strand.
    """
