import re
   
def find_orfs_reverse(dna: str):
    reverse = convertDnaToReversComplemet(dna)
    start_pos = findStartPos(dna)

def findStartPos(dna: str):
    for match in re.finditer("ATG",dna):
        start_pos = match.start()
        return start_pos



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

