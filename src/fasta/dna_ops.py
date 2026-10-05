class DNASequence:
    def __init__(self,sequence: str):
        self.sequence = sequence

    def complement(self):
        complement_map = str.maketrans("ATCG","TAGC")
        return self.sequence.translate(complement_map)
    def reverse_complement(self):
        return self.complement()[::-1]
    def to_rna(self):
        return self.sequence.replace('T','U')
    def gc_content(self):
        if len(self.sequence) == 0:
            return 0.0
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return (gc_count / len(self.sequence)) * 100
