
class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
    def complement(self):
        result = ''
        for base in self.sequence:
            if base == 'A':
                result += "T"
            elif base == "T":
                result += "A"
            elif base == "C":
                result += "G"
            elif base == "G":
                result += "C"
        return result
    def reverse_complement(self):
        complement = self.complement()
        result = ""

        for base in reversed(complement):
            result += base

        return result
    def to_rna(self):
        result=''
        for base in self.sequence:
            if base=='T':
                result +="U"
            else:
                result +=base
        return result

    def gc_content(self):
        gc = self.sequence.count('C') + self.sequence.count('G')
        result = (gc/ len(self.sequence)) * 100
        return result
