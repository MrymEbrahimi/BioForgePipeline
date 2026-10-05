class Protein:
    """Represent a protein sequence.

    Attributes:
        sequence: Amino acid sequence of the protein.

        Calculate the molecular weight of the protein.

        Args:
            weights_dict: Dictionary mapping amino acids to their weights.

        Returns:
            The total molecular weight of the protein.
        """
    def __init__(self,sequence):
        self.sequence = sequence
    def weight(self, weights_dict):
        total_weight = 0
        for amino_acid in self.sequence:
            if amino_acid not in weights_dict:
                raise ValueError(f"weight not found for amino acid {amino_acid}")
            total_weight += weights_dict[amino_acid]
        return total_weight