import re

   
def find_orfs_reverse(dna: str):
    start_pos = findStartPos(dna)

def findStartPos(dna: str):
    for match in re.finditer("ATG",dna):
        start_pos = match.start()
        return start_pos


