import re
   
def find_orfs_reverse(dna: str):
    start = findStartPos(dna)
    for frame in range(3):
         
    

def findStartPos(dna: str) -> int:
    reverseComplementdna = convertDnaToReversComplemet(dna)
    for match in re.finditer("ATG",reverseComplementdna):
        start_pos = match.start()
        return start_pos
    
def findFrames(dna:str):
    start = findStartPos(dna)
    return -start

def findStop(dna:str):
    start = findStartPos(dna)
    reverseComplementdna = convertDnaToReversComplemet(dna)
    pattern = r"TAA|TAG|TGA"
    for match in re.finditer(pattern,reverseComplementdna):
            if match.start() > start:
                stop_pos = match.start()
                return stop_pos
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

