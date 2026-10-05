import re
from .orf import ORF

def find_orfs_reverse(dna: str):
    orfList = []  
    reverseComplement = convertDnaToReversComplement(dna)
    start = findStartPos(reverseComplement)  
    stop = findStop(reverseComplement)  
    
    if start == -1:  
        return orfList
    
    if stop is None:
        orf = ORF(
            strand="Reverse",
            frame=findFrames(reverseComplement),  
            start_pos=len(dna) - start,  
            protein=reverseComplement[start:],  
            is_complete=False
        )
        orfList.append(orf)
    else:
        orf = ORF(
            strand="Reverse",
            frame=findFrames(reverseComplement),
            start_pos=len(dna) - start,
            protein=reverseComplement[start:stop+3], 
            is_complete=True
        )
        orfList.append(orf)
    
    return orfList  

def findStartPos(dna: str) -> int:
    for match in re.finditer("ATG", dna):
        return match.start()
    return -1


def findFrames(dna: str):
    start = findStartPos(dna)
    if start == -1:
        return 0
    return start % 3


def findStop(dna: str):
    start = findStartPos(dna)
    if start == -1:
        return None
    pattern = r"TAA|TAG|TGA"
    for match in re.finditer(pattern, dna):
        if match.start() > start:
            return match.start()
    return None


def convertDnaToReversComplement(dna: str):
    dna = dna.upper()
    reverse = dna[::-1]
    dnaTranslator = str.maketrans("ATCG", "TAGC")
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
